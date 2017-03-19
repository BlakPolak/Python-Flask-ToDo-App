/**
 * Created by ppolak on 19.03.17.
 */


function changeBackground(){
    if ($('body').hasClass('firstBackground')) {
            $('body').addClass('secondBackground').removeClass('firstBackground');
        }
        else
        {
            $('body').addClass('firstBackground').removeClass('secondBackground');
        }

};

function changeFont(){
    if ($('body').hasClass('firstFont')) {
            $('body').addClass('secondFont').removeClass('firstFont');
        }
        else
        {
            $('body').addClass('firstFont').removeClass('secondFont');
        }

};
// font-family: sans-serif;
//     font-size: 14px;