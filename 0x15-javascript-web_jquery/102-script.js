$(document).ready(function () {
    $('#btn_translate').click(function () {
      const languageCode = $('#language_code').val();
        $.ajax({
        url: `https://www.fourtonfish.com/hellosalut/hello/?lang`,
        success: function (data) {
          $('#hello').text(data.hello);
        }
      });
    });
  });
