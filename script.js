$(document).ready(function() {
    // Fetch the text from the Python script
    $.ajax({
        url: 'http://your-python-server.com/path/to/your/python/script',
        type: 'GET',
        success: function(response) {
            // Update the text in the HTML page
            $('#textPlaceholder').text(response.text);
        },
        error: function() {
            console.log('Failed to fetch text from Python script.');
        }
    });
});
