# External Visit Tracking

This feature tracks external link visits from your Jekyll site and provides analytics on which external sites your visitors are clicking on.

## Features

- **Automatic Tracking**: Tracks clicks on external links automatically
- **Social Media Focus**: Primarily tracks social media and academic platform links
- **Local Storage**: Data is stored locally in the browser's localStorage
- **Analytics Integration**: Sends events to Google Analytics (if configured)
- **Dashboard**: Interactive dashboard to view statistics
- **Export**: Export data as JSON for further analysis

## Configuration

The tracking can be configured in `_config.yml`:

```yaml
# External Visit Tracking
external_visits:
  enabled                : true          # Enable/disable tracking
  track_social_links     : true          # Track social media links
  track_all_external     : false         # Track all external links (not just social)
  analytics_integration  : true          # Send events to Google Analytics
  debug                  : false         # Enable debug logging
```

## Tracked Platforms

The system automatically tracks visits to these platforms:

- **Social Media**: GitHub, LinkedIn, Twitter, Facebook, Instagram, YouTube
- **Academic**: Google Scholar, ResearchGate, ORCID
- **Professional**: Keybase, Bitbucket, Stack Overflow
- **Creative**: Dribbble, Pinterest, Flickr, CodePen
- **Other**: Wikipedia, Steam, SoundCloud, and more

## Usage

### Dashboard

Visit `/external-visits/` to see the interactive dashboard with:

- Total visit count
- Unique domains visited
- Today's visits
- Top domains by visit count
- Recent visits with timestamps

### Widget

Include the widget on any page:

```liquid
{% include external-visits-widget.html %}
```

### Programmatic Access

Access the tracking data via JavaScript:

```javascript
// Get statistics
const stats = ExternalVisitTracker.getStats();

// Manually track a visit
ExternalVisitTracker.trackVisit('https://example.com', 'Example Site');

// Clear all data
ExternalVisitTracker.clearData();
```

## Data Structure

The tracking data is stored as an array of visit objects:

```javascript
{
  url: "https://github.com/username",
  domain: "github.com",
  label: "Github",
  timestamp: "2024-01-01T12:00:00.000Z",
  date: "2024-01-01"
}
```

## Privacy

- Data is stored locally in the browser's localStorage
- No data is sent to external servers (except Google Analytics events if enabled)
- Users can clear their data at any time
- Data is limited to the last 1000 visits to prevent storage bloat

## Customization

### Adding New Platforms

To track additional platforms, add them to the `socialDomains` array in `assets/js/external-visits.js`:

```javascript
const socialDomains = [
  // ... existing domains
  'your-new-platform.com'
];
```

### Custom Tracking

For custom tracking scenarios, use the programmatic API:

```javascript
// Track a specific external link
window.trackExternalVisit('https://custom-site.com', 'Custom Label');
```

## Troubleshooting

### Debug Mode

Enable debug mode in `_config.yml` to see console logs:

```yaml
external_visits:
  debug: true
```

### Check if Tracking is Working

1. Open browser developer tools
2. Go to Console tab
3. Click on an external link
4. You should see a log message if debug is enabled

### Data Not Persisting

- Check if localStorage is enabled in the browser
- Ensure the site is served over HTTPS (localStorage may be restricted on HTTP)

## Browser Support

- Modern browsers with localStorage support
- JavaScript must be enabled
- Works on desktop and mobile browsers

## Integration with Analytics

If Google Analytics is configured, external link clicks will be sent as events:

- **Category**: "External Link"
- **Action**: "Click"
- **Label**: Domain name

This allows you to track external link engagement in your Google Analytics dashboard.
