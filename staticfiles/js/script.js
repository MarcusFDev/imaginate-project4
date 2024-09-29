$(document).ready(function(){
    $('#nav-home').hover(
        function() {
            // Mouse enters the element
            $(this).find('i').addClass('icon-beat');
        },
        function() {
            // Mouse leaves the element
            $(this).find('i').removeClass('icon-beat');
        }
    );
    $('#nav-stories').hover(
        function() {
            // Mouse enters the element
            $(this).find('i').addClass('icon-bounce');
        },
        function() {
            // Mouse leaves the element
            $(this).find('i').removeClass('icon-bounce');
        }
    );
    $('#nav-profile').hover(
        function() {
            // Mouse enters the element
            $(this).find('i').addClass('icon-beat');
        },
        function() {
            // Mouse leaves the element
            $(this).find('i').removeClass('icon-beat');
        }
    );
});

$(document).ready(function() {

    $('.btn-close').on('click', function() {
        console.log("Received Request.");
        
        // Add the fade-out animation to #info-alert
        $('#info-alert').addClass('animate__animated animate__fadeOutUp');

        // Start sliding up the #info-section
        $('#info-section').slideUp(400, function() {
            $(this).addClass('hidden');
        });

        console.log("Request Complete.");
    });
});

$(document).ready(function() {

    console.log('Page Loaded, animations intialized')

    $('#imaginate-titles h1').addClass('animate__animated animate__fadeInUp');
    console.log('Animation 1 finished')
    setTimeout(function() {
        $('#imaginate-titles h3').addClass('animate__animated animate__fadeInUp');
    }, 500);
    console.log('Animation 2 finished')
});

$(document).ready(function() {
    $('#signupForm').on('submit', function(event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $('#signupModal').modal('hide');
                    location.reload();
                } else {
                    $('#signupModal').modal('show');
                }
            },
            error: function(xhr, status, error) {
                console.log("Something went wrong. Error:", error);
                $('#signupModal').modal('show');
            }
        });
    });
});
