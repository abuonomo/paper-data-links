(function() {
  function displaySearchResults(results, store) {
    var searchResults = document.getElementById('results-container');
    if (results.length) {
      var appendString = '';
      for (var i = 0; i < results.length; i++) {
        var item = store[results[i].ref];
        appendString += '<li><a href="' + item.url + '"><strong>' + item.bibcode + '</strong> - ' + item.title + '</a></li>';
      }
      searchResults.innerHTML = appendString;
    } else {
      searchResults.innerHTML = '<li>No results found</li>';
    }
  }

  function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');
      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  var searchTerm = getQueryVariable('query');

  if (searchTerm) {
    document.getElementById('search-input').setAttribute("value", searchTerm);
    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('bibcode', { boost: 5 });
      this.field('content');
    });

    for (var key in window.store) {
      idx.add({
        'id': key,
        'title': window.store[key].title,
        'bibcode': window.store[key].bibcode,
        'content': window.store[key].content
      });
    }

    var results = idx.search(searchTerm);
    displaySearchResults(results, window.store);
  }

  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      document.getElementById('search-input').focus();
    }
  });

  document.getElementById('search-input').addEventListener('input', function() {
    var searchTerm = this.value;
    var results = idx.search(searchTerm);
    displaySearchResults(results, window.store);
  });
})();