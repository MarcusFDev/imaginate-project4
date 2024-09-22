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
