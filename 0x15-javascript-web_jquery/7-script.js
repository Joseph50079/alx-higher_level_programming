// script fetch json name from url api
url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, function (data) {
  $('DIV#character').text(data.name);
});
