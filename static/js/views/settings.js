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
                if ($(row).data('id')) {
                    itemstodelete.push($(row).data('id'));
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

            var type = $(this).find('.select-dropdown').val().toLowerCase();
            var url = $(this).find('.url').val();
            var api_key = $(this).find('.api_key').val();
            var id = $(this).data('id');
            if (!type || !url || !api_key) {
                return
            }

            $.ajax('/settings/addIndexer?type=' + type + '&url=' + url + '&api_key=' + api_key + '&id=' + id).done(function(response){

                try {

                    var data = JSON.parse(response);
                }
                catch(e){

                    console.log(response);
                }

                if (data.success) {

                    showNotification('Settings saved');
                }
                else {

                    showNotification('Error');
                }
            });
        });

        for (var i in itemstodelete) {

            $.ajax('/settings/removeIndexer?id=' + itemstodelete[i]).done(function(response){

                var data = JSON.parse(response);

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

        $(this).material_select();
    });
})