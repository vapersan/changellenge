$(document).ready(function(){
    $('input[name="sort"]').click(function (){
        $('input[name="sort"]').each((k, v) => {
            $(v).next().css('background-color','rgb(255,255,255)');
            $(v).next().css('color','black');
            $(v).parent().css('background-color','rgb(255,255,255)');
        });
        if($(this).prop('checked') === true)
        {
            $(this).next().css('background-color','rgb(23,162,184)');
            $(this).next().css('color','white');
            $(this).parent().css('background-color','rgb(23,162,184)');
        }
    });
    $('.heart').click(function(){
        if($(this).css('filter') === 'grayscale(1)'){
           $(this).css('filter', 'grayscale(0)'); 
        }else{
            $(this).css('filter', 'grayscale(1)');
        }
    });
});