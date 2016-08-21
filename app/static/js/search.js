function onSearch(e) {
  var query = document.getElementById("search-box").value;

  search(query);

}

function search(query) {
  xhr = new XMLHttpRequest();
  xhr.open("POST", "/search", true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var json = JSON.parse(xhr.responseText);
      var resultEl = document.getElementById("search-results");
      resultEl.innerText = query;
    }
  }
  var data = JSON.stringify({"query": query});
  xhr.send(data);
}

var searchEl = document.getElementById("search-box");
searchEl.addEventListener("input", onSearch, true);
