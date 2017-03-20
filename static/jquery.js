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
    if ($('span').hasClass('firstFont')) {
            $('span').addClass('secondFont').removeClass('firstFont');
        }
        else
        {
            $('span').addClass('firstFont').removeClass('secondFont');
        }

};

function addThingToDo(){
    var newform= '<h3>ADD NEW THING TO DO</h3>'+
        '<form action="/add" method="POST">'+
        '<input type="text" name="name" id="name" placeholder="Thing to do" autofocus, required>' +
        '<input type="submit" value="Add"> </form>';
    $(".thingToDo").append(newform)
}


function editThingToDo(item_id){
    var newform= '<h3>UPDATE THING TO DO</h3>'+
                '<form action="/edit/{{ item_id }}" method="POST">'+
                '<input type="text" name="update" id="name" placeholder="Edit name" autofocus, required>' +
                '<input type="submit" value="Update">'+
                '</form>';
    $('.editThingToDo').append(newform)
}