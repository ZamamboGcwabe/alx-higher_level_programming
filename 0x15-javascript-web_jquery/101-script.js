// Add a new item to the list
// Remove the last item from the list
// Clear all items from the list
$(document).ready(function() {
    
    $('#add_item').click(function() {
        $('.my_list').append('<li>Item</li>');
    });

    $('#remove_item').click(function() {
        $('.my_list li:last').remove();
    });

    $('#clear_list').click(function() {
        $('.my_list').empty();
    });
});
