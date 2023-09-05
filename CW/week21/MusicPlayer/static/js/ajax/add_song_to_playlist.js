$('body').on('submit', '#selectPlaylist', function (event) {
    event.preventDefault();
    let self = $(this)
    let playlist_option = self.find("[name='playlist_option']")
    let playlist_input = self.find("[name='playlist_input']")
    console.log('1')
    playlist_input.val(playlist_option.val())
    console.log(playlist_input.val())
    $.ajax({
        type: 'Post',
        url: self.attr('action'),
        data: self.serialize(),
        success: function (response) {
            console.log(response.message)
            self.find('#msg1').text('Comment created successfully')
        },
        error: function (response) {
            console.log('', response)
        }
    })
    console.log('test 2')
    setTimeout(function () {
        $('body').off('submit', '#creat_comment');
        self.find('#msg1').text('')
    }, 2000);
})