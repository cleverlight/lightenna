---
layout: tag-page
author_profile: false
header:
  overlay_image: /assets/images/cloudlake_mirror_23878_1920x.jpg
---

<!-- content in pages/index_content.md -->
{% include_relative _pages/index_content.md %}

<!-- make header image into half-bleed -->
<style>
  h1.page__title {
    display: none;
  }
  div.masthead {
    height: 0;
  }
  nav.greedy-nav {
    background: transparent;
  }
</style>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var vh = $(window).height(); 
    $('div.page__hero--overlay').css('height',(vh/2) + 'px');
  });
</script>