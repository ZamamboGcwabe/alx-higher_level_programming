$(document).ready(function() {
    function fetchHello() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(fetchHello);

    $('#language_code').keypress(function(event) {
        if (event.key === 'Enter') {
            fetchHello();
        }
    });
});
