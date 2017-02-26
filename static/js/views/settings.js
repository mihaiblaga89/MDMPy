$(document).ready(function(){

    $("#shutdown").click(function() {

//        $.ajax("shutdown")
//          .done(function() {

                $('#modal-alert').iziModal('open');
//          })
    });

    $("#restart").click(function() {

        $.ajax("restart")
          .done(function() {
            alert( "success" );
          })
    });
})