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

    var itemstodelete = [];

    $('.repeat').each(function() {
        $(this).repeatable_fields({
            row_count_placeholder: '(row-count-placeholder)',
            is_sortable: false,
            before_remove : function(container, row){
                var url = $(row).find('.url').val();
                if (url != "") {
                    itemstodelete.push(url);
                }
            }
        });
    });

    $('#save').click(function() {

        $('.row').not('.template').each(function(element) {

            type = $(this).find('.type').val();
            url = $(this).find('.url').val();
            api_key = $(this).find('.api_key').val();

            $.ajax('/settings/addIndexer?type=' + type + '&url=' + url + '&api_key=' + api_key).done(function(response){

                var data = JSON.parse(response);
                console.log(data);

                if (data.success) {
                    showNotification('Settings saved');
                }
                else {
                    showNotification('Error');
                }
            });
        });

        for (var i in itemstodelete) {

            $.ajax('/settings/removeIndexer?url=' + itemstodelete[i]).done(function(response){

                var data = JSON.parse(response);
                console.log(data);

                if (data.success) {
                    showNotification('Settings saved');
                }
                else {
                    showNotification('Error');
                }
            });

            itemstodelete.splice(i, 1);
        }


    });
})