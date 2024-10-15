// ====================================
// base.html Functions
// ====================================


$(document).ready(function() {

    // Define icon class for each nav element.
    const iconClasses = {
        '#nav-home': 'icon-beat',
        '#nav-library': 'icon-shake',
        '#nav-stories': 'icon-bounce',
        '#nav-profile': 'icon-beat'
    };

    // Iterate over elements & set up hover.
    $.each(iconClasses, function(selector, className) {
        $(selector).hover(
            function() {
                // On Mouse enter Add class.
                $(this).find('i').toggleClass(className, true);
            },
            function() {
                // On Mouse leave Remove class.
                $(this).find('i').toggleClass(className, false);
            }
        );
    });
});


// ====================================
// user_profile.html Functions
// ====================================


$(document).ready(function() {
    
    // Handle the close button click.
    $('.btn-close').on('click', function() {
        
        // Targets #info-alert & applies animation.
        $('#info-alert').addClass('animate__animated animate__fadeOutUp');

        // Slides #info-section & applies hidden class.
        $('#info-section').slideUp(400, function() {
            $(this).addClass('hidden');
        });

    });
});


$(document).ready(function() {

    // Handle click detected on element.
    $('.danger-overlay').on('click', function() {

        var $overlay = $(this);

        // Add animation class to the overlay element.
        $overlay.addClass('animate__animated animate__fadeOut');

        // Remove the overlay element after animation.
        setTimeout(function() {
            $overlay.remove();
        }, 1500);
    });
});


$(document).ready(function() {
    $('.submit-aboutme').on('click', function(event) {
        event.preventDefault();
        
        var form = $(this).closest('form');
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        var modal = form.closest('.modal-content');
        var errormsg = form.find('.error-msg');
        
        // Send the aboutme data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                csrfmiddlewaretoken: csrfToken,
                bio: form.find('textarea[name="bio"]').val()
            },
            dataType: 'json',
            success: function(data) {
                if (data.status === 'success') {
                    modal.removeClass('border-glow-red');
                    $('.pf-description p').html(data.bio);
                    location.reload();
                } else {

                    modal.html(data.form);
                    modal.addClass('border-glow-red');
                    setTimeout(function() {
                        modal.removeClass('border-glow-red');
                    }, 5000);

                    errormsg.removeClass('hidden');
                    setTimeout(function() {
                        errormsg.addClass('hidden');
                    }, 5000);
                }
            },
            error: function(xhr, status, error) {

                modal.addClass('border-glow-red');
                setTimeout(function() {
                    modal.removeClass('border-glow-red');
                }, 5000);

                errormsg.removeClass('hidden');
                setTimeout(function() {
                    errormsg.addClass('hidden');
                }, 5000);
            }
        });
    });
});


// ====================================
// home_page.html Functions
// ====================================


$(document).ready(function() {

    // Targets Home title applies animation class.
    $('#imaginate-titles h1').addClass('animate__animated animate__fadeInUp');
    
    // Targets Home title subheading applies animation class.
    setTimeout(function() {
        $('#imaginate-titles h3').addClass('animate__animated animate__fadeInUp');
    }, 500);
});


// ====================================
// index.html / Library Page Functions
// ====================================


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

    // Handle the filter button click.
    $('.filter-btn').on('click', function() {

        // Toggle hidden class on element.
        $('.filter-select').toggleClass('hidden');
      });
});


// ====================================
// story_page.html Functions
// ====================================


$(document).ready(function() {

    var $textareas = $('.comment-input');
    
    /** 
     * Automatically resizes all <textarea> elements with the class 'comment-input'
     * to fit their content by adjusting the height based on their scroll height.
     */
    function autoResize() {
        
        // Loop over each <textarea> & adjust height content height.
        $textareas.each(function() {
            $(this).css('height', 'auto');
            $(this).css('height', this.scrollHeight + 'px');
        });
    }

    // Attach the resize logic to the input event of each <textarea>.
    $textareas.on('input', function() {
        $(this).css('height', 'auto');
        $(this).css('height', this.scrollHeight + 'px');
    });
    
    // Initial resize on DOM load.
    autoResize();
});


$(document).ready(function() {
    
    // Listen for clicks on elements 'upvote-btn' class.
    $(document).on('click', '.upvote-btn', function() {
        
        // Toggle class on the <i> element within the clicked '.upvote-btn' element.
        $(this).find('i').toggleClass('fa-solid text-danger animate__animated animate__bounceIn');
    });
});


$(document).ready(function() {

    // On Mouse Enter over element with 'delete-btn' class, add classes.
    $(document).on('mouseenter', '.delete-btn', function() {
        $(this).find('i').addClass('icon-shake text-danger');
    })
    // On Mouse Leave over element with 'delete-btn' class, remove classes.
    .on('mouseleave', '.delete-btn', function() {
        $(this).find('i').removeClass('icon-shake text-danger');
    });
});


$(document).ready(function() {

    // Handle the upvote comment button click.
    $('.upvote-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var commentId = form.find('input[name="comment_id"]').val();
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the upvote data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                comment_id: commentId,
                csrfmiddlewaretoken: csrfToken
             },
            dataType: 'json',
            success: function(data) {
                // Update the comment upvote count.
                $(form).find('.upvote-count').text(data.upvotes);
                
                // Toggle icon based on comment Upvote or Remove Upvote.
                if (data.action == 'added') {
                    $(form).find('.upvote-btn i').removeClass('fa-regular').addClass('fa-solid').addClass('text-danger');
                    $('.comment-upvoted-alert').fadeIn().delay(3000).fadeOut();
                } else if (data.action == 'removed') {
                    $(form).find('.upvote-btn i').removeClass('fa-solid text-danger').addClass('fa-regular');
                    $('.comment-unvoted-alert').fadeIn().delay(3000).fadeOut();
                }
            }
        });
    });
});


$(document).ready(function() {  
    // Handle the delete comment button click.
    $('.delete-confirm-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the delete data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: { 
                comment_id: form.find('input[name="comment_id"]').val(), 
                csrfmiddlewaretoken: csrfToken 
            },
            dataType: 'json',
            success: function(data) {
                // Delete comment from page.
                if (data.success) {
                    $(form).closest('.comment').remove();
                    $('.comment-delete-alert').fadeIn().delay(3000).fadeOut();
                    // Close the modal
                    form.closest('.modal').modal('hide');
                }
            }
        });
    });
});


$(document).ready(function() {

    // Handle the edit & cancel button click.
    $('.edit-btn, .cancel-btn').on('click', function(event) {
        event.preventDefault();
        var commentId = $(this).data('comment-id');
        var editCommentField = $(this).closest('li').find('.edited-comment');
        var commentBody = $(this).closest('li').find('.comment-list-body');
        var parentLi = editCommentField.closest('li');
        
        // Toggles class on targetted elements.
        editCommentField.toggleClass('hidden');
        commentBody.toggleClass('hidden');
        parentLi.toggleClass('border-glow');
    });
});


$(document).ready(function() {

    // Handle the save comment button click.
    $('.save-btn').on('click', function(e) {
        e.preventDefault();
        var button = $(this);
        var form = button.closest('li').find('form');
        var commentBody = form.find('textarea[name="body"]').val();
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the save data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'body': commentBody
            },
            dataType: 'json',
            success: function(data) {
                console.log("Save Button detected" ,data);

                // Add Classes to targetted elements
                button.closest('li').find('.comment-list-body').text(commentBody);
                var editCommentField = button.closest('li').find('.edited-comment');
                var commentBodyElement = button.closest('li').find('.comment-list-body');
                var parentLi = editCommentField.closest('li');

                editCommentField.toggleClass('hidden');
                commentBodyElement.toggleClass('hidden');
                parentLi.toggleClass('border-glow');

                $('.comment-saved-alert').fadeIn().delay(3000).fadeOut();
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
                
                // Add Error Classes to targetted elements.
                var parentLi = button.closest('li');
                parentLi.toggleClass('border-glow-red');
                setTimeout(function() {
                    parentLi.toggleClass('border-glow-red');
                }, 5000);

                var errorMessage = button.closest('li').find('.error-message');
                errorMessage.toggleClass('hidden');
                setTimeout(function() {
                    errorMessage.toggleClass('hidden');
                }, 5000);

                $('.comment-error-alert').fadeIn().delay(3000).fadeOut();
            }
        });
    });
});


$(document).ready(function() {

    // Handle the add comment button click.
    $('.comment-new-submit').on('click', function(e) {
        e.preventDefault();
        var button = $(this);
        var form = button.closest('form');
        var commentBody = form.find('textarea[name="body"]').val();
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the save data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'body': commentBody
            },
            dataType: 'json',
            success: function(data) {
                console.log(data);
                location.reload()
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
                
                // Add Error Classes to targetted elements.
                var commentField = button.closest('form').find('textarea[name="body"]');
                commentField.toggleClass('border-glow-red');
                setTimeout(function() {
                    commentField.toggleClass('border-glow-red');
                }, 5000);

                var errorMessage = button.closest('form').find('.error-message');
                errorMessage.toggleClass('hidden');
                setTimeout(function() {
                    errorMessage.toggleClass('hidden');
                }, 5000);

                $('.comment-error-alert').fadeIn().delay(3000).fadeOut();
            }
        });
    });
});


$(document).ready(function() {

    // Handle the upvote story button click.
    $('.story-upvote-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var storySlug = form.find('input[name="story_upvote"]').val();
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the upvote data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                story_slug: storySlug,
                csrfmiddlewaretoken: csrfToken
             },
            dataType: 'json',
            success: function(data) {
                // Update the story upvote count.
                $(form).find('.story-upvote-count').text(data.upvotes);
                
                // Toggle icon based on story Upvote or Remove Upvote.
                if (data.action == 'added') {
                    $(form).find('.story-upvote-div').removeClass('story-upvote').addClass('story-upvote-active');
                    $(form).find('.story-upvote-btn i').removeClass('fa-regular').addClass('fa-solid').addClass('text-danger');
                    $('.story-upvoted-alert').fadeIn().delay(3000).fadeOut();
                } else if (data.action == 'removed') {
                    $(form).find('.story-upvote-div').removeClass('story-upvote-active').addClass('story-upvote');
                    $(form).find('.story-upvote-btn i').removeClass('fa-solid text-danger').addClass('fa-regular');
                    $('.story-unvoted-alert').fadeIn().delay(3000).fadeOut();
                }
            }
        });
    });
});


// ====================================
// my_stories.html Functions
// ====================================


$(document).ready(function() {

    // Handle the is_private button click.
    $('.private-btn').on('click', function(event) {
        event.preventDefault();
        var form = $(this).closest('form');
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the is_private data via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: {
                csrfmiddlewaretoken: csrfToken
             },
            dataType: 'json',
            success: function(data) {

                // Toggle icon based on story private status.
                if (data.action == 'Made public') {
                    $(form).find('.private-btn i').removeClass('fa-eye-slash text-danger').addClass('fa-eye text-success');
                } else if (data.action == 'Made private') {
                    $(form).find('.private-btn i').removeClass('fa-eye text-success').addClass('fa-eye-slash text-danger');
                }
            }
        });
    });
});


$(document).ready(function() {

    // Handle the form submission for story deletion
    $('body').on('submit', '.story-delete-form', function(event) {
        event.preventDefault();

        // The form that was submitted
        var form = $(this);
        var csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();
        
        // Send the delete request via AJAX.
        $.ajax({
            type: 'POST',
            url: form.attr('action'),  // The action URL for deletion
            data: { 
                csrfmiddlewaretoken: csrfToken  // Pass CSRF token to the request
            },
            dataType: 'json',
            success: function(data) {
                if (data.success) {
                    // Remove the deleted story element from the page dynamically
                    $('#story-' + data.slug).remove();

                    // Close the modal
                    form.closest('.modal').modal('hide');
                } else if (data.error) {
                    alert(data.error);  // Handle error response
                }
            },
            error: function(xhr, status, error) {
                console.log("Something went wrong: ", error);  // Handle server errors
            }
        });
    });
});


