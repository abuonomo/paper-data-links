---
layout: default
title: Papers
---

# Papers

{% for paper in site.pages %}
  {% if paper.path contains 'papers/' and paper.name == 'README.md' %}
    - [{{ paper.title }}]({{ paper.url | relative_url }})
  {% endif %}
{% endfor %}