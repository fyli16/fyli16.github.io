---
layout: single
# title: "Research"
permalink: /research/
author_profile: true
---

<div style="padding: 2rem; border-radius: 12px; margin-bottom: 2rem; background-image: radial-gradient(circle at 25% 25%, rgba(139, 92, 246, 0.1) 0%, transparent 50%), radial-gradient(circle at 75% 75%, rgba(59, 130, 246, 0.1) 0%, transparent 50%); background-size: 100px 100px;">
  <div style="position: relative; margin-bottom: 2rem;">
    <h1 style="background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Research</h1>
    <p style="font-size: 1.1rem; color: #6b7280; margin-top: 0.5rem;">Bridging AI/ML with cutting-edge plasma physics and fusion energy research</p>
  </div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
  {% for post in site.research %}
    <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07); border: 1px solid #e5e7eb; transition: all 0.3s ease-in-out;">
      <div style="border-bottom: 1px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1rem;">
        <h3 style="margin: 0; color: #3b82f6;">
          {% if post.title contains "Alfvén" %}
            <i class="fas fa-wave-square"></i>
          {% elsif post.title contains "Vacuum" %}
            <i class="fas fa-atom"></i>
          {% elsif post.title contains "Laser" %}
            <i class="fas fa-bolt"></i>
          {% elsif post.title contains "Plasma" %}
            <i class="fas fa-fire"></i>
          {% else %}
            <i class="fas fa-flask"></i>
          {% endif %}
          {{ post.title }}
        </h3>
        {% if post.excerpt %}
          <div style="margin-top: 0.5rem;">
            {{ post.excerpt }}
          </div>
        {% endif %}
      </div>
      <div>
        <div style="margin-bottom: 1rem;">
          {% if post.title contains "Alfvén" %}
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #8b5cf6; color: white;">Wave Physics</span>
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #3b82f6; color: white;">Simulation</span>
          {% elsif post.title contains "Vacuum" %}
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #8b5cf6; color: white;">Particle Acceleration</span>
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #3b82f6; color: white;">Laser Physics</span>
          {% elsif post.title contains "Laser" %}
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #8b5cf6; color: white;">Optics</span>
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #3b82f6; color: white;">Plasma Interaction</span>
          {% elsif post.title contains "Plasma" %}
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #8b5cf6; color: white;">Plasma Physics</span>
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #3b82f6; color: white;">Fusion Energy</span>
          {% else %}
            <span style="display: inline-block; padding: 0.25em 0.6em; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 6px; background-color: #3b82f6; color: white;">Research</span>
          {% endif %}
        </div>
        
        <div style="margin-bottom: 1rem;">
          {{ post.content | strip_html | truncatewords: 30 }}
        </div>
        
        <a href="{{ post.url }}" style="display: inline-block; padding: 0.75rem 1.5rem; font-size: 0.9rem; font-weight: 600; text-align: center; text-decoration: none; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s ease-in-out; background: #8b5cf6; color: white;">
          <i class="fas fa-arrow-right"></i> Read More
        </a>
      </div>
    </div>
  {% endfor %}
</div>

<div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07); border: 1px solid #e5e7eb; transition: all 0.3s ease-in-out; text-align: center; background: linear-gradient(135deg, rgba(139, 92, 246, 0.05) 0%, rgba(59, 130, 246, 0.05) 100%);">
  <div>
    <h3 style="color: #8b5cf6; margin-bottom: 1rem;">
      <i class="fas fa-microscope"></i> Research Highlights
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
      <div style="text-align: center; padding: 1rem;">
        <i class="fas fa-paper-plane" style="font-size: 2rem; color: #8b5cf6; margin-bottom: 0.5rem;"></i>
        <div style="font-weight: bold; color: #8b5cf6;">40+</div>
        <div style="color: #6b7280; font-size: 0.9rem;">Publications</div>
      </div>
      <div style="text-align: center; padding: 1rem;">
        <i class="fas fa-citation" style="font-size: 2rem; color: #3b82f6; margin-bottom: 0.5rem;"></i>
        <div style="font-weight: bold; color: #3b82f6;">~800</div>
        <div style="color: #6b7280; font-size: 0.9rem;">Citations</div>
      </div>
      <div style="text-align: center; padding: 1rem;">
        <i class="fas fa-grant" style="font-size: 2rem; color: #14b8a6; margin-bottom: 0.5rem;"></i>
        <div style="font-weight: bold; color: #14b8a6;">NASA/DOE</div>
        <div style="color: #6b7280; font-size: 0.9rem;">Funded Research</div>
      </div>
    </div>
    <p style="margin-bottom: 1.5rem;">
      My research spans the intersection of AI/ML and plasma physics, with applications in fusion energy, 
      space science, and particle acceleration. I'm particularly interested in developing computational 
      methods that leverage machine learning for plasma diagnostics and control.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="/publications/" style="display: inline-block; padding: 0.75rem 1.5rem; font-size: 0.9rem; font-weight: 600; text-align: center; text-decoration: none; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s ease-in-out; background: #8b5cf6; color: white; margin: 0.25rem;">
        <i class="fas fa-book"></i> View Publications
      </a>
      <a href="/talks/" style="display: inline-block; padding: 0.75rem 1.5rem; font-size: 0.9rem; font-weight: 600; text-align: center; text-decoration: none; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s ease-in-out; background: #3b82f6; color: white; margin: 0.25rem;">
        <i class="fas fa-presentation"></i> Talks & Presentations
      </a>
      <a href="mailto:lif02501@gmail.com" style="display: inline-block; padding: 0.75rem 1.5rem; font-size: 0.9rem; font-weight: 600; text-align: center; text-decoration: none; border: none; border-radius: 8px; cursor: pointer; transition: all 0.2s ease-in-out; background: #14b8a6; color: white; margin: 0.25rem;">
        <i class="fas fa-envelope"></i> Collaborate
      </a>
    </div>
  </div>
</div>

