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
            },
            after_add : function(new_row) {
                $(new_row).find('.type').last().material_select();
//                $('select').material_select();
            }
        });
    });

    $('#save').click(function() {

        $('.row').not('.template').each(function(element) {

            type = $(this).find('.select-dropdown').val().toLowerCase();
            url = $(this).find('.url').val();
            api_key = $(this).find('.api_key').val();
            console.log(type, url, api_key);

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

    $('tr.row:not(.template)').find('select').each(function() {
        console.log(this);
        $(this).material_select();
    });
})