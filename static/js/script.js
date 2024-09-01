$(document).ready(function(){
    $('#nav-home').hover(
        function() {
            // Mouse enters the element
            $(this).addClass('fa-beat');
        },
        function() {
            // Mouse leaves the element
            $(this).removeClass('fa-beat');
        }
    );
    $('#nav-stories').hover(
        function() {
            // Mouse enters the element
            $(this).addClass('fa-bounce');
        },
        function() {
            // Mouse leaves the element
            $(this).removeClass('fa-bounce');
        }
    );
    $('#nav-profile').hover(
        function() {
            // Mouse enters the element
            $(this).addClass('fa-beat');
        },
        function() {
            // Mouse leaves the element
            $(this).removeClass('fa-beat');
        }
    );
});

