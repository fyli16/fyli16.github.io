---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="ai-pattern" style="padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
  <div class="section-header">
    <h1 class="gradient-text">Publications</h1>
    <p style="font-size: 1.1rem; color: #6b7280; margin-top: 0.5rem;">Selected peer-reviewed journal papers and research publications</p>
  </div>
</div>

{% if author.googlescholar %}
<div class="card animate-card" style="margin-bottom: 2rem;">
  <div class="card-body" style="text-align: center;">
    <p style="margin-bottom: 1rem;">
      <i class="ai ai-google-scholar" style="font-size: 2rem; color: var(--ml-blue); margin-right: 0.5rem;"></i>
      You can also find my articles on <a href="{{author.googlescholar}}" class="focus-modern" target="_blank">my Google Scholar profile</a>.
    </p>
  </div>
</div>
{% endif %}

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
  {% for post in site.publications reversed %}
    <div class="card animate-card">
      <div class="card-header">
        <h3>
          {% if post.venue contains "Nature" %}
            <i class="fas fa-atom"></i>
          {% elsif post.venue contains "Physical Review" %}
            <i class="fas fa-wave-square"></i>
          {% elsif post.venue contains "Applied Physics" %}
            <i class="fas fa-bolt"></i>
          {% else %}
            <i class="fas fa-flask"></i>
          {% endif %}
          {{ post.title }}
        </h3>
        <div style="margin-top: 0.5rem;">
          {% if post.venue contains "Nature" %}
            <span class="badge badge-ai">High Impact</span>
          {% elsif post.venue contains "Physical Review" %}
            <span class="badge badge-ml">Physics</span>
          {% elsif post.venue contains "Applied Physics" %}
            <span class="badge badge-ds">Applied Science</span>
          {% else %}
            <span class="badge badge-research">Research</span>
          {% endif %}
          <span class="badge badge-research">{{ post.venue }}</span>
        </div>
      </div>
      <div class="card-body">
        <div style="margin-bottom: 1rem;">
          <p style="color: #6b7280; font-style: italic;">{{ post.excerpt }}</p>
        </div>
        
        <div style="margin-bottom: 1rem;">
          <strong>Citation:</strong><br>
          <code style="font-size: 0.9rem; background: rgba(139, 92, 246, 0.1); padding: 0.5rem; border-radius: 4px; display: block; margin-top: 0.5rem;">{{ post.citation }}</code>
        </div>
        
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          {% if post.paperurl %}
            <a href="{{ post.paperurl }}" class="btn btn-modern btn-outline" target="_blank">
              <i class="fas fa-file-pdf"></i> Read Paper
            </a>
          {% endif %}
          <span style="color: #6b7280; font-size: 0.9rem; align-self: center;">
            <i class="fas fa-calendar"></i> {{ post.date | date: "%B %Y" }}
          </span>
        </div>
      </div>
    </div>
  {% endfor %}
</div>

<div class="card animate-card" style="text-align: center; background: linear-gradient(135deg, rgba(139, 92, 246, 0.05) 0%, rgba(59, 130, 246, 0.05) 100%);">
  <div class="card-body">
    <h3 style="color: var(--ai-purple); margin-bottom: 1rem;">
      <i class="fas fa-chart-line"></i> Publication Statistics
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
      <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2rem; font-weight: bold; color: var(--ai-purple);">{{ site.publications.size }}</div>
        <div style="color: #6b7280; font-size: 0.9rem;">Publications</div>
      </div>
      <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2rem; font-weight: bold; color: var(--ml-blue);">~800</div>
        <div style="color: #6b7280; font-size: 0.9rem;">Total Citations</div>
      </div>
      <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2rem; font-weight: bold; color: var(--ds-teal);">14</div>
        <div style="color: #6b7280; font-size: 0.9rem;">h-index</div>
      </div>
      <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2rem; font-weight: bold; color: var(--primary-color);">22</div>
        <div style="color: #6b7280; font-size: 0.9rem;">i10-index</div>
      </div>
    </div>
    <p style="margin-bottom: 1.5rem;">
      My research spans plasma physics, laser-plasma interactions, particle acceleration, and AI/ML applications in scientific computing.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="https://scholar.google.com/citations?user=8jVlsdoAAAAJ&hl=en" class="btn btn-modern btn-ai" target="_blank">
        <i class="ai ai-google-scholar"></i> Google Scholar
      </a>
      <a href="https://www.researchgate.net/profile/Feiyu-Li-4" class="btn btn-modern btn-ml" target="_blank">
        <i class="ai ai-researchgate"></i> ResearchGate
      </a>
      <a href="/research/" class="btn btn-modern btn-ds">
        <i class="fas fa-microscope"></i> Research Areas
      </a>
    </div>
  </div>
</div>
