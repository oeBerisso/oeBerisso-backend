$('.ui.dropdown').dropdown();

$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;

$('.ui.accordion')
  .accordion()
;
$('.ui.accordion active').click(() => $(this).removeClass('active'));
$('.ui.accordion').click(() => $(this).adClass('active'));