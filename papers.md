---
layout: default
title: All Papers
---

# All Papers

<ul class="paper-list">
{% assign sorted_pages = site.pages | sort: 'path' | reverse %}
{% for paper in sorted_pages %}
  {% if paper.path contains 'papers/' and paper.name == 'README.md' %}
    <li>
      <a href="{{ paper.url | relative_url }}">{{ paper.bibcode }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>
