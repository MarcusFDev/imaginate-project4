$(document).ready(function() {
    $('#aboutme_textarea').summernote({
        toolbar: [
            ['font', ['bold', 'italic', 'underline', 'clear']],
            ['ul'],
            ['ol'],
            
        ],
        colors: [
            ['#FF0000', '#00FF00', '#0000FF', '#FFFF00'],
            ['#FFA500', '#800080', '#FFFFFF']
        ],
        iframe: false,
        height: 600,
        toolbar_BS5: true,
    });
});


$(document).ready(function() {
    $('#aboutmemodal').on('shown.bs.modal', function () {
        if (!$('#aboutme_textarea').hasClass('summernote')) {
            $('#aboutme_textarea').summernote({
                focus: true
            });
        }
    });
  
    // Optional: Destroy Summernote when modal is hidden (to avoid re-initialization issues)
    $('#aboutmemodal').on('hidden.bs.modal', function () {
        if ($('#aboutme_textarea').hasClass('summernote')) {
            $('#aboutme_textarea').summernote('destroy');
        }
    });
});
