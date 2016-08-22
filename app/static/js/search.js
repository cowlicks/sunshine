function onSearch(e) {
  var query = document.getElementById("search-box").value;

  search(query);
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

var searchEl = document.getElementById("search-box");
searchEl.addEventListener("input", onSearch, true);
