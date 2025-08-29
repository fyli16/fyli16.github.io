---
title: "External Visits Dashboard"
permalink: /external-visits/
author_profile: false
layout: single
---

<div class="ai-pattern" style="padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
  <div class="section-header">
    <h1 class="gradient-text">External Visits Analytics</h1>
    <p style="font-size: 1.1rem; color: #6b7280; margin-top: 0.5rem;">Real-time tracking of external link interactions from your website</p>
  </div>
</div>

<div id="external-visits-dashboard">
  <div class="card animate-card" style="margin-bottom: 2rem;">
    <div class="card-header">
      <h3><i class="fas fa-chart-bar"></i> Overview Statistics</h3>
    </div>
    <div class="card-body">
      <div class="stat-cards">
        <div class="stat-card">
          <div class="stat-number" id="total-visits">-</div>
          <div class="stat-label">Total Visits</div>
        </div>
        <div class="stat-card">
          <div class="stat-number" id="unique-domains">-</div>
          <div class="stat-label">Unique Domains</div>
        </div>
        <div class="stat-card">
          <div class="stat-number" id="today-visits">-</div>
          <div class="stat-label">Today's Visits</div>
        </div>
      </div>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
    <div class="card animate-card">
      <div class="card-header">
        <h3><i class="fas fa-globe"></i> Top Domains</h3>
      </div>
      <div class="card-body">
        <div id="top-domains" class="stats-list"></div>
      </div>
    </div>

    <div class="card animate-card">
      <div class="card-header">
        <h3><i class="fas fa-clock"></i> Recent Visits</h3>
      </div>
      <div class="card-body">
        <div id="recent-visits" class="stats-list"></div>
      </div>
    </div>
  </div>

  <div class="card animate-card">
    <div class="card-header">
      <h3><i class="fas fa-cogs"></i> Dashboard Actions</h3>
    </div>
    <div class="card-body">
      <div class="stats-actions">
        <button id="refresh-stats" class="btn btn-modern btn-ml">
          <i class="fas fa-sync-alt"></i> Refresh Stats
        </button>
        <button id="clear-data" class="btn btn-modern btn-outline" style="border-color: #ef4444; color: #ef4444;">
          <i class="fas fa-trash"></i> Clear All Data
        </button>
        <button id="export-data" class="btn btn-modern btn-ds">
          <i class="fas fa-download"></i> Export Data
        </button>
      </div>
    </div>
  </div>
</div>

<style>
.stat-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.stat-card {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
  border: 1px solid rgba(139, 92, 246, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease-in-out;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(139, 92, 246, 0.15);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  background: linear-gradient(135deg, var(--ai-purple) 0%, var(--ml-blue) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #6b7280;
  font-size: 0.9rem;
  font-weight: 500;
}

@media (max-width: 768px) {
  .stats-details {
    grid-template-columns: 1fr;
  }
}

.stats-list {
  margin-top: 1rem;
}

.stats-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid #e5e7eb;
  transition: all 0.2s ease-in-out;
}

.stats-item:hover {
  background-color: rgba(139, 92, 246, 0.05);
  border-radius: 8px;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.stats-item:last-child {
  border-bottom: none;
}

.stats-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn-modern {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  background: var(--ml-blue);
  color: white;
}

.btn-modern:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
  text-decoration: none;
}

.btn-modern:focus {
  outline: 2px solid var(--ml-blue);
  outline-offset: 2px;
}

.btn-modern.btn-outline {
  background: transparent;
  border: 2px solid;
  color: inherit;
}

.btn-modern.btn-outline:hover {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

.btn-modern.btn-ds {
  background: var(--ds-teal);
}

.btn-modern.btn-ds:hover {
  box-shadow: 0 4px 12px rgba(20, 184, 166, 0.4);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  function updateDashboard() {
    if (typeof ExternalVisitTracker === 'undefined') {
      console.log('External Visit Tracker not loaded');
      return;
    }

    const stats = ExternalVisitTracker.getStats();
    
    // Update overview stats
    document.getElementById('total-visits').textContent = stats.total;
    document.getElementById('unique-domains').textContent = Object.keys(stats.byDomain).length;
    
    // Calculate today's visits
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('today-visits').textContent = stats.byDate[today] || 0;

    // Update top domains
    const topDomains = Object.entries(stats.byDomain)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 10);
    
    const topDomainsHtml = topDomains.map(([domain, count]) => 
      `<div class="stats-item">
        <span style="font-weight: 500;">${domain}</span>
        <span style="font-weight: bold; color: var(--ai-purple);">${count}</span>
      </div>`
    ).join('');
    
    document.getElementById('top-domains').innerHTML = topDomainsHtml;

    // Update recent visits
    const recentVisitsHtml = stats.recent.map(visit => 
      `<div class="stats-item">
        <span style="font-weight: 500;">${visit.label}</span>
        <span style="color: #6b7280; font-size: 0.9rem;">${new Date(visit.timestamp).toLocaleDateString()}</span>
      </div>`
    ).join('');
    
    document.getElementById('recent-visits').innerHTML = recentVisitsHtml;
  }

  // Refresh stats button
  document.getElementById('refresh-stats').addEventListener('click', updateDashboard);

  // Clear data button
  document.getElementById('clear-data').addEventListener('click', function() {
    if (confirm('Are you sure you want to clear all external visit data? This action cannot be undone.')) {
      ExternalVisitTracker.clearData();
      updateDashboard();
    }
  });

  // Export data button
  document.getElementById('export-data').addEventListener('click', function() {
    const stats = ExternalVisitTracker.getStats();
    const dataStr = JSON.stringify(stats, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'external-visits-data.json';
    link.click();
    URL.revokeObjectURL(url);
  });

  // Initial load
  updateDashboard();
});
</script>
