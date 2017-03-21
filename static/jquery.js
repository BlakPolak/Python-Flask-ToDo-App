/**
 * Created by ppolak on 19.03.17.
 */


function changeBackground(){
    /**Function allows to change background image*/
    if ($('body').hasClass('firstBackground')) {
            $('body').addClass('secondBackground').removeClass('firstBackground');
        }
        else
        {
            $('body').addClass('firstBackground').removeClass('secondBackground');
        }

};

function changeFont(){
    /**Function allows to change font*/
    if ($('span').hasClass('firstFont')) {
            $('span').addClass('secondFont').removeClass('firstFont');
        }
        else
        {
            $('span').addClass('firstFont').removeClass('secondFont');
        }

};

function addThingToDo(){
    /**Function allows to add new thing*/
    var newform= '<h3>ADD NEW THING TO DO</h3>'+
        '<form action="/add" method="POST">'+
        '<input type="text" name="name" id="name" placeholder="Thing to do" autofocus, required>' +
        '<input type="submit" value="Add"> </form>';
    $(".thingToDo").append(newform)
}