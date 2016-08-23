function debouncer(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this, args = arguments;
    var later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

function parseSearch(results) {
  var out = "<ul>";
  var rlen = results.length;

  for (var i = 0; i < rlen; i++) {
      var dept = results[i];
      out += "<li><a href=\"/department/" + dept + "\">" + dept + "</a></li>";
  }
  out += "</ul>";
  return out;
}

function search(query) {
  xhr = new XMLHttpRequest();
  xhr.open("POST", "/search", true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var json = JSON.parse(xhr.responseText);
      var resultEl = document.getElementById("search-results");
      resultEl.innerHTML = parseSearch(json);
    }
  }
  var data = JSON.stringify({"query": query});
  xhr.send(data);
}

function onSearch() {
  var query = document.getElementById("search-box").value;
  search(query);
}

var searchEl = document.getElementById("search-box");
searchEl.addEventListener("input", debouncer(onSearch, 250), true);
