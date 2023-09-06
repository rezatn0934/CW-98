function myselect() {
    const config = {
        search: true
    };
    dselect(document.querySelector('#dselect-example'), config);
}

myselect()

$('body').on('submit', '#createPlaylistForm', function (event) {
    event.preventDefault();
    self = $(this)
    $.ajax({
        type: 'POST',
        url: self.attr('action'),
        data: self.serialize(),
        success: function (response) {
            self.find('#creatPlaylist').val('')
            $('#dselect-example').append($(
                '<option>',
                {
                    value: response.id,
                    text: response.title
                })).val(response.id)
            myselect()
            $('#createPlaylistForm').animate()
            console.log('success')
        },
        error: function (response) {
            console.log('error', response)
        }
    })
})