    $(function() {
        $.ajax({
            url: '/getWish',
            type: 'GET',
            success: function(res) {
                console.log(res);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });