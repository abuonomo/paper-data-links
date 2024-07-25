---
layout: default
title: VSO Instrument Data Links
---

# Welcome to VSO Instrument Data Links

This repository stores information about the VSO instruments used in scientific papers.

## Recent Papers

<div class="paper-list">
{% assign sorted_pages = site.pages | sort: 'path' | reverse %}
{% for paper in sorted_pages limit:10 %}
  {% if paper.path contains 'papers/' and paper.name == 'README.md' %}
    <a href="{{ paper.url | relative_url }}" class="paper-button">{{ paper.bibcode }}</a>
  {% endif %}
{% endfor %}
</div>

[View All Papers]({{ '/papers.html' | relative_url }})