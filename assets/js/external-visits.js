// External Visit Tracker
(function() {
  'use strict';

  // Configuration
  const config = {
    storageKey: 'externalVisits',
    trackSocialLinks: true,
    trackAllExternal: false,
    analyticsIntegration: true,
    debug: false
  };

  // Initialize tracking
  function initExternalVisitTracker() {
    if (config.debug) {
      console.log('External Visit Tracker initialized');
    }

    // Track arrival from external referrer
    trackReferrerIfExternal();

    // Track external link clicks
    document.addEventListener('click', function(e) {
      const link = e.target.closest('a');
      if (!link) return;

      const href = link.href;
      if (!href) return;

      // Check if it's an external link
      if (isExternalLink(href)) {
        // Check if it's a social link we want to track
        if (config.trackSocialLinks && isSocialLink(href)) {
          trackVisit(href, link.textContent.trim());
        }
        // Or track all external links if enabled
        else if (config.trackAllExternal) {
          trackVisit(href, link.textContent.trim());
        }
      }
    });

    // Track programmatically (for analytics integration)
    window.trackExternalVisit = function(url, label) {
      trackVisit(url, label);
    };
  }

  // Track external referrer on page load
  function trackReferrerIfExternal() {
    try {
      const referrer = document.referrer;
      if (!referrer) return;
      if (isExternalLink(referrer)) {
        // Save a visit against the referrer domain
        trackVisit(referrer, 'Referrer');
      }
    } catch (e) {
      // ignore
    }
  }

  // Check if link is external
  function isExternalLink(href) {
    try {
      const url = new URL(href);
      const currentHost = window.location.hostname;
      return url.hostname !== currentHost && url.hostname !== '';
    } catch (e) {
      return false;
    }
  }

  // Check if link is a social media link
  function isSocialLink(href) {
    const socialDomains = [
      'github.com',
      'linkedin.com',
      'twitter.com',
      'facebook.com',
      'instagram.com',
      'youtube.com',
      'scholar.google.com',
      'researchgate.net',
      'orcid.org',
      'keybase.io',
      'bitbucket.org',
      'stackoverflow.com',
      'dribbble.com',
      'pinterest.com',
      'foursquare.com',
      'steamcommunity.com',
      'soundcloud.com',
      'flickr.com',
      'codepen.io',
      'vine.co',
      'weibo.com',
      'wikipedia.org'
    ];

    try {
      const url = new URL(href);
      return socialDomains.some(domain => url.hostname.includes(domain));
    } catch (e) {
      return false;
    }
  }

  // Track a visit
  function trackVisit(url, label) {
    const visits = loadVisitData();
    const domain = extractDomain(url);
    const timestamp = new Date().toISOString();
    
    // Create visit record
    const visit = {
      url: url,
      domain: domain,
      label: label || domain,
      timestamp: timestamp,
      date: timestamp.split('T')[0]
    };

    // Add to visits array
    visits.push(visit);

    // Keep only last 1000 visits to prevent storage bloat
    if (visits.length > 1000) {
      visits.splice(0, visits.length - 1000);
    }

    // Save to localStorage
    saveVisitData(visits);

    // Send to analytics if enabled
    if (config.analyticsIntegration && window.ga) {
      window.ga('send', 'event', 'External Link', 'Click', domain);
    }

    if (config.debug) {
      console.log('Tracked external visit:', visit);
    }
  }

  // Extract domain from URL
  function extractDomain(url) {
    try {
      const urlObj = new URL(url);
      return urlObj.hostname.replace('www.', '');
    } catch (e) {
      return 'unknown';
    }
  }

  // Load visit data from localStorage
  function loadVisitData() {
    try {
      const data = localStorage.getItem(config.storageKey);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Error loading visit data:', e);
      return [];
    }
  }

  // Save visit data to localStorage
  function saveVisitData(visits) {
    try {
      localStorage.setItem(config.storageKey, JSON.stringify(visits));
    } catch (e) {
      console.error('Error saving visit data:', e);
    }
  }

  // Get visit statistics
  function getVisitStats() {
    const visits = loadVisitData();
    const stats = {
      total: visits.length,
      byDomain: {},
      byDate: {},
      recent: visits.slice(-10).reverse()
    };

    visits.forEach(visit => {
      // Count by domain
      stats.byDomain[visit.domain] = (stats.byDomain[visit.domain] || 0) + 1;
      
      // Count by date
      stats.byDate[visit.date] = (stats.byDate[visit.date] || 0) + 1;
    });

    return stats;
  }

  // Export functions to global scope
  window.ExternalVisitTracker = {
    getStats: getVisitStats,
    trackVisit: trackVisit,
    clearData: function() {
      localStorage.removeItem(config.storageKey);
    }
  };

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initExternalVisitTracker);
  } else {
    initExternalVisitTracker();
  }

})();
