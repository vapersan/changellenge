$(document).ready(function(){
    $('input[name="sort"]').click(function (){
        if($(this).next().css('background-color') == 'rgba(0, 0, 0, 0)'){
            $(this).next().css('background-color','rgb(23,162,184)');
            $(this).next().css('color','white');
            $(this).parent().css('background-color','rgb(23,162,184)');
        }else{
            $(this).next().css('background-color','rgba(0, 0, 0, 0)');
            $(this).next().css('color','black');
            $(this).parent().css('background-color','rgba(0, 0, 0, 0)');                       
        }
        
    });
    $('.heart').click(function(){
        if($(this).css('filter') === 'grayscale(1)'){
           $(this).css('filter', 'grayscale(0)'); 
        }else{
            $(this).css('filter', 'grayscale(1)');
        }
    });
    $('.heart-rev').click(function(){
        
        if($(this).css('filter') === 'grayscale(0)'){
           $(this).css('filter', 'grayscale(1)');
            $(this).parent().parent().parent().parent().fadeOut(200);
        }else{
            $(this).css('filter', 'grayscale(0)');
        }
    });
    $('input[name="planets"]').amsifySuggestags({
        type : 'amsify',
        suggestions: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupitor', 'Uranus', 'Neptune', 'Pluto'],
        whiteList: true
    });
    $('#save-btn').click(function(){
        var status = $('.stat-stl').css('display');
        if(status === 'none'){
            $('.stat-stl').fadeIn(500);
            $('.stat-stl').fadeOut(3000);
        }
    });
});