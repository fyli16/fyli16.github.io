---
title: "External Visits Dashboard"
permalink: /external-visits/
author_profile: false
layout: single
---

This dashboard shows statistics for external link visits from your site.

<div id="external-visits-dashboard">
  <div class="stats-overview">
    <h3>Overview</h3>
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

  <div class="stats-details">
    <div class="stats-section">
      <h3>Top Domains</h3>
      <div id="top-domains" class="stats-list"></div>
    </div>

    <div class="stats-section">
      <h3>Recent Visits</h3>
      <div id="recent-visits" class="stats-list"></div>
    </div>
  </div>

  <div class="stats-actions">
    <button id="refresh-stats" class="btn btn--primary">Refresh Stats</button>
    <button id="clear-data" class="btn btn--danger">Clear All Data</button>
    <button id="export-data" class="btn btn--info">Export Data</button>
  </div>
</div>

<style>
.stats-overview {
  margin-bottom: 2rem;
}

.stat-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.stat-card {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #6c757d;
  font-size: 0.9rem;
}

.stats-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .stats-details {
    grid-template-columns: 1fr;
  }
}

.stats-section {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
}

.stats-list {
  margin-top: 1rem;
}

.stats-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #e9ecef;
}

.stats-item:last-child {
  border-bottom: none;
}

.stats-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
}

.btn--primary {
  background: #007bff;
  color: white;
}

.btn--danger {
  background: #dc3545;
  color: white;
}

.btn--info {
  background: #17a2b8;
  color: white;
}

.btn:hover {
  opacity: 0.8;
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
        <span>${domain}</span>
        <span>${count}</span>
      </div>`
    ).join('');
    
    document.getElementById('top-domains').innerHTML = topDomainsHtml;

    // Update recent visits
    const recentVisitsHtml = stats.recent.map(visit => 
      `<div class="stats-item">
        <span>${visit.label}</span>
        <span>${new Date(visit.timestamp).toLocaleDateString()}</span>
      </div>`
    ).join('');
    
    document.getElementById('recent-visits').innerHTML = recentVisitsHtml;
  }

  // Refresh stats button
  document.getElementById('refresh-stats').addEventListener('click', updateDashboard);

  // Clear data button
  document.getElementById('clear-data').addEventListener('click', function() {
    if (confirm('Are you sure you want to clear all external visit data?')) {
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
