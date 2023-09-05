$('body').on('submit', '#creat_comment', function (event) {
    event.preventDefault();
    event.preventDefault();
    let self = $(this)
    $.ajax({
        type: 'Post',
        url: self.attr('action'),
        data: self.serialize(),
        success: function (response) {
            console.log(response.message)
            self.find('#id_content').val('')
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