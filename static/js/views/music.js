$(document).ready(function() {

    function search() {

        var query = $("#searchInput").val();

        if (query == '') {

            return;
        }

        $.ajax('/music/search?query=' + query).done(function(response){

            var result = JSON.parse(response)
            console.log(result);

            if (result.success) {

                console.log('enters')
                var data = result.data.tracks.items;

                $('#searchResults').empty();

                for (var i in data) {

                    var imageurl = data[i].album.images[0].url;

                    var injection = '<div data-album="' + data[i].album.name + '" data-id="' + data[i].id + '" data-name="' + data[i].name + '" data-artist="' + data[i].artists[0].name + '" class="searchResult pure-u-1 pure-u-md-1-3"> \
                        <img src="' + imageurl + '" class="pure-img searchResult-image"/> \
                        <div class="searchResult-title"> \
                            <span>' + data[i].artists[0].name + ' - ' + data[i].name + '</span> \
                        </div> \
                        <div class="searchResult-release"><span>' + (data[i].duration_ms / 1000) + '</span></div> \
                        <div class="searchResult-album"><span>' + data[i].album.name + '</span></div> \
                        <div class="searchResult-preview"> \
                            <audio controls="" name="media"><source src="' + data[i].preview_url + '" type="audio/mpeg"></audio> \
                        </div> \
                        <div class="searchResult-options"> \
                            <span>Quality</span> \
                            <select> \
                                <option value="hq">Loseless</option> \
                                <option value="mp3">MP3</option> \
                            </select> \
                            <label><input type="checkbox" id="allow-youtube" value="1"> Allow YouTube download</label> \
                        </div> \
                        <button id="add" class="pure-button"><i class="fa fa-plus-circle"></i> Add</button> \
                    </div>';

                    $('#searchResults').append(injection);
                }

                $('.searchResult #add').click(function() {

                    var allow_youtube = true;
                    var quality = 'mp3';
                    var title = $(this).closest('.searchResult').data('name');
                    var id = $(this).closest('.searchResult').data('id');
                    var artist = $(this).closest('.searchResult').data('artist');
                    var album = $(this).closest('.searchResult').data('album');
                    var data = {
                        title : title,
                        id: id,
                        allow_youtube : allow_youtube,
                        quality : quality,
                        artist : artist,
                        album : album
                    }

                    $.ajax({
                        url : '/music/add',
                        type : "POST",
                        data : data,
                        contentType : "application/json"
                    }).done(function(response){

                        var result = JSON.parse(response);
                        if (result.success) {

                            alert('done');
                        }
                        else {

                            alert('sum-ting wong');
                        }
                     });
                })
            }
        });
    }


    $('#searchInput').bind("enterKey",function(e){

        search();
    });

    $('#searchInput').keyup(function(e){

        if(e.keyCode == 13) {

            $(this).trigger("enterKey");
        }
    });

    $("#search").click(function() {

        search();
    });
});