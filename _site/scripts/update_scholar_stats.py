#!/usr/bin/env python3

import os
import sys
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError as exc:  # pragma: no cover
    raise SystemExit(f"Missing dependency: {exc}. Install with `pip install requests`.")

AUTHOR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "8jVlsdoAAAAJ")
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "scholar_stats.yml"


def _find_first_value(data, keys):
    if isinstance(data, dict):
        for key in keys:
            if key in data:
                return data[key]
        for value in data.values():
            found = _find_first_value(value, keys)
            if found is not None:
                return found
    elif isinstance(data, list):
        for item in data:
            found = _find_first_value(item, keys)
            if found is not None:
                return found
    return None


def _find_metric(data, keys):
    seen = set()

    def walk(node):
        if id(node) in seen:
            return None
        seen.add(id(node))

        if isinstance(node, dict):
            lowered = {str(k).lower().replace(" ", "_"): v for k, v in node.items()}
            for key in keys:
                key_l = str(key).lower().replace(" ", "_")
                if key_l in lowered:
                    return lowered[key_l]
            for v in node.values():
                found = walk(v)
                if found is not None:
                    return found
        elif isinstance(node, list):
            for item in node:
                found = walk(item)
                if found is not None:
                    return found
        return None

    return walk(data)


def _to_int(value):
    if value is None:
        return 0
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        cleaned = value.replace(",", "").replace("+", "")
        try:
            return int(float(cleaned))
        except ValueError:
            return 0
    if isinstance(value, dict):
        return _to_int(value.get("value", value.get("count", 0)))
    return 0


def fetch_from_serpapi(author_id: str):
    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        return None

    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "hl": "en",
        "api_key": api_key,
    }

    response = requests.get("https://serpapi.com/search.json", params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    if data.get("error"):
        raise RuntimeError(f"SerpApi error: {data.get('error')}")

    author = data.get("author") or data.get("profile") or {}
    cited_by = data.get("cited_by", {})
    table = cited_by.get("table", []) if isinstance(cited_by, dict) else []

    def parse_table_metric(metric_name):
        for entry in table:
            if not isinstance(entry, dict):
                continue
            for key, value in entry.items():
                key_name = str(key).lower().replace("-", "_")
                if key_name in {metric_name, metric_name.replace("_", ""), metric_name.replace("_index", "index")}:
                    if isinstance(value, dict):
                        return value.get("all", value.get("total", value.get("count")))
        return None

    total_value = (
        parse_table_metric("citations")
        or _find_metric(data, ["cited_by", "citations", "total_citations", "all", "all_citations", "citation_count"])
        or _find_metric(cited_by, ["citations", "total_citations", "all", "all_citations", "citation_count"])
        or _find_metric(author, ["citations", "total_citations", "all", "all_citations", "citation_count"])
    )
    h_value = (
        parse_table_metric("h_index")
        or _find_metric(data, ["h_index", "hindex", "h-index", "hIndex", "all_h_index"])
        or _find_metric(cited_by, ["h_index", "hindex", "h-index", "hIndex", "all_h_index"])
        or _find_metric(author, ["h_index", "hindex", "h-index", "hIndex", "all_h_index"])
    )
    h10_value = (
        parse_table_metric("i10_index")
        or _find_metric(data, ["h10_index", "i10_index", "i10index", "h10index", "i10-index"])
        or _find_metric(cited_by, ["h10_index", "i10_index", "i10index", "h10index", "i10-index"])
        or _find_metric(author, ["h10_index", "i10_index", "i10index", "h10index", "i10-index"])
    )

    stats = {
        "total_citations": _to_int(total_value),
        "h_index": _to_int(h_value),
        "h10_index": _to_int(h10_value),
    }

    if stats["total_citations"] == 0 and stats["h_index"] == 0 and stats["h10_index"] == 0:
        debug_dump = {
            "top_level_keys": sorted(data.keys()),
            "author_keys": sorted(author.keys()),
            "cited_by": cited_by,
        }
        print("Debug SerpApi payload:")
        print(json.dumps(debug_dump, indent=2, default=str)[:5000])
        raise RuntimeError(
            "SerpApi returned a response but no Scholar stat fields were found. "
            f"Top-level keys: {sorted(data.keys())[:20]} | author keys: {sorted(author.keys())[:20]}"
        )

    return stats


def fetch_from_scholarly(author_id: str):
    try:
        from scholarly import scholarly
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "scholarly is not installed. Install with `pip install scholarly` or set SERPAPI_KEY."
        ) from exc

    try:
        author = next(scholarly.search_author_id(author_id))
        filled = scholarly.fill(author)
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"Unable to fetch scholar data for author_id {author_id!r}: {exc}") from exc

    stats = {
        "total_citations": _to_int(filled.get("citedby", filled.get("cited_by", 0))),
        "h_index": _to_int(filled.get("hindex", filled.get("h_index", 0))),
        "h10_index": _to_int(filled.get("i10index", filled.get("i10_index", 0))),
    }

    if stats["total_citations"] == 0 and stats["h_index"] == 0 and stats["h10_index"] == 0:
        raise RuntimeError(
            f"Scholarly returned no usable stats for author_id {author_id!r}. "
            f"Result keys: {sorted(filled.keys())[:20]}"
        )

    return stats


def write_yaml(stats):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    content = (
        f"total_citations: {stats['total_citations']}\n"
        f"h_index: {stats['h_index']}\n"
        f"h10_index: {stats['h10_index']}\n"
        f"last_updated: \"{timestamp}\"\n"
    )
    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


def main():
    try:
        stats = fetch_from_serpapi(AUTHOR_ID)
        if stats is None:
            stats = fetch_from_scholarly(AUTHOR_ID)
        if not stats:
            raise RuntimeError("No scholar stats returned.")
        write_yaml(stats)
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
