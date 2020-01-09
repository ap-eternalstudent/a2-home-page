;
(function ($) {
  "use strict";

  $(function () {
    $('#contactForm').validate({
      rules: {
        name: {
          required: true,
          minlength: 2,
          maxlength: 50,
        },
        email: {
          email: true,
          required: true,
          maxlength: 50
        },
        subject: {
          required: true,
          minlength: 3,
          maxlength: 100
        },
        message: {
          required: true,
          minlength: 20,
          maxlength: 500
        }
      }
    })
  });
  
})(jQuery)