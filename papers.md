---
layout: default
title: All Papers
---

# All Papers

<div class="paper-list">
{% assign sorted_pages = site.pages | sort: 'path' | reverse %}
{% for paper in sorted_pages %}
  {% if paper.path contains 'papers/' and paper.name == 'README.md' %}
    <a href="{{ paper.url | relative_url }}" class="paper-button">{{ paper.bibcode }}</a>
  {% endif %}
{% endfor %}
</div>