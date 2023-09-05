
$('body').on('submit', '#like_form', function (event) {
    event.preventDefault();
    let self = $(this)
    let like_button = self.find("[name='like_input']")
    let like_button_value = like_button.val()
    $.ajax({
        type: 'POST',
        url: self.attr('action'),
        data: self.serialize(),
        success: function (response) {
            self.find('#like_count').text(response.like_count)

            if (like_button_value == 'unlike') {
                like_button.val('like')
                self.find('.bi').removeClass('like_red')
            } else {
                like_button.val('unlike')
                self.find('.bi').addClass('like_red')
            }
        },
        error: function (response) {
            console.log('error', response)
        }
    })

})
