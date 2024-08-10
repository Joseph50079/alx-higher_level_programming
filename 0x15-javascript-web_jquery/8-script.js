// script for fectching al movies title
url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, function (data) {
  data.films.forEach(function (filmUrl) {
    $.getJSON(filmUrl, function (filmData) {
      $('UL#list_movies').append('<li>' + filmData.title + '<li>');
    });
  });
});
