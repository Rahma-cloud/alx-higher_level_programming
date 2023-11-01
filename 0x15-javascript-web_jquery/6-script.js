$(document).ready(function () {
    $('#update_header').click(function () {
        const newHeader = $('<p>New Header!!!</p>');
        $('header').append(newHeader);
    });
});
