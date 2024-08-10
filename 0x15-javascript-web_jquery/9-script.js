// Script fetch from url and return value to id=hello of html
const url = "https://hellosalut.stefanbohacek.dev/?lang=fr"
$(document).ready(function () {
	$.getJSON(url, function (data) {
		$('DIV#hello').text(data.hello);
	});
});
