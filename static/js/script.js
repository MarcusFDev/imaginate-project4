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
        $('#filter-select').toggleClass('hidden');
      });
});

$(document).ready(function() {
    var $textareas = $('.comment-input');

    function autoResize() {

        $textareas.each(function() {
            $(this).css('height', 'auto');
            $(this).css('height', this.scrollHeight + 'px');
        });
    }

    $textareas.on('input', function() {
        $(this).css('height', 'auto');
        $(this).css('height', this.scrollHeight + 'px');
    });

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

                if (data.action == 'added') {
                    $(form).find('.upvote-btn i').removeClass('fa-regular').addClass('fa-solid').addClass('text-danger');
                } else if (data.action == 'removed') {
                    $(form).find('.upvote-btn i').removeClass('fa-solid text-danger').addClass('fa-regular');
                }
            }
        });
    });
});

$(document).ready(function() {
    $('.delete-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: { 
                comment_id: form.find('input[name="comment_id"]').val(), 
                csrfmiddlewaretoken: csrfToken 
            },
            dataType: 'json',
            success: function(data) {
                if (data.success) {
                    $(form).closest('.comment').remove();
                }
            }
        });
    });
});

$(document).ready(function() {
    $('.edit-btn, .cancel-btn').on('click', function(event) {
        event.preventDefault();
        var commentId = $(this).data('comment-id');
        var editCommentField = $(this).closest('li').find('.edited-comment');
        var commentBody = $(this).closest('li').find('.comment-list-body');
        var parentLi = editCommentField.closest('li');

        editCommentField.toggleClass('hidden');
        commentBody.toggleClass('hidden');
        parentLi.toggleClass('border-glow');
    });
});

$(document).ready(function() {
    $('.save-btn').on('click', function(e) {
        e.preventDefault();
        var commentId = $(this).closest('form').find('input[name="comment_id"]').val();
        var form = $(this).closest('form');
        var commentBody = $(this).closest('form').find('textarea[name="body"]').val();
        var csrfToken = $(this).closest('form').find('input[name="csrfmiddlewaretoken"]').val();
        var button = $(this);

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'body': commentBody
            },
            success: function(data) {
                console.log(data);

                button.closest('li').find('.comment-list-body').text(commentBody);
                var editCommentField = button.closest('li').find('.edited-comment');
                var commentBodyElement = button.closest('li').find('.comment-list-body');
                var parentLi = editCommentField.closest('li');

                editCommentField.toggleClass('hidden');
                commentBodyElement.toggleClass('hidden');
                parentLi.toggleClass('border-glow');
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
            }
        });
    });
});
