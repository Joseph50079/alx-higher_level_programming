// add items to header with div add_item is clicked
$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
