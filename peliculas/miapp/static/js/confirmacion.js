$(function(){
    $('#search-form :input')
      .change(function(){
        var $input = $(this);
        if ($input.val() === '')
        {
          $input.removeClass('filledInputs');
        }
        else
        {
          $input.addClass('filledInputs');
        }
      });
  });