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
    $('#nav-library').hover(
        function() {
            // Mouse enters the element
            $(this).find('i').addClass('icon-shake');
        },
        function() {
            // Mouse leaves the element
            $(this).find('i').removeClass('icon-shake');
        }
    )
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

    const $searchIcon = $('#search-icon');
    const $searchInput = $('#search-input');
    const $form = $searchIcon.closest('form');

    $searchIcon.on('click', function(event) {
        event.preventDefault();
        $searchInput.focus();
        $form.submit();
    });
});

$(document).ready(function() {
    
    $('#filter-button').on('click', function() {
        console.log('Filter button triggered')
        $('#filter-select').toggleClass('hidden');
      });
});

$(document).ready(function() {
    var $textarea = $('#comment-input');
    
    // Function to resize the textarea
    function autoResize() {
        console.log('resize function triggered')
        // Reset height to auto to calculate new height
        $textarea.css('height', 'auto');
        // Set height to scroll height
        $textarea.css('height', $textarea[0].scrollHeight + 'px');
    }
    
    // Bind the input event to the textarea
    $textarea.on('input', autoResize);
    
    // Initial resize
    autoResize();
});

$(document).ready(function() {

    $(document).on('click', '.upvote-btn', function() {

        $(this).find('i').toggleClass('fa-solid text-danger animate__animated animate__bounceIn');
    });
});

$(document).ready(function() {

    $(document).on('mouseenter', '.delete-btn', function() {

        $(this).find('i').addClass('icon-shake text-danger');
    }).on('mouseleave', '.delete-btn', function() {

        $(this).find('i').removeClass('icon-shake text-danger');
    });
});


$(document).ready(function() {
    $('.upvote-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var commentId = form.find('input[name="comment_id"]').val();
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                comment_id: commentId,
                csrfmiddlewaretoken: csrfToken
             },
            dataType: 'json',
            success: function(data) {
                
                $(form).find('.upvote-count').text(data.upvotes);
            }
        });
    });
});
