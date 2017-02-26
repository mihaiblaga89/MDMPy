$(document).ready(function() {

    $("#search").click(function() {

        var query = $("#searchInput").val();

        $.ajax('/dashboard/search?query=' + query).done(function(response){

            var result = JSON.parse(response)
            console.log(result);
            console.log(result.success);

            if (result.success) {

                var data = result.data;

                for (var i in data) {

                    var spliturl = data[i].cover.url.split('t_thumb');

                    var imageurl = spliturl[0] + 'w_300,h_300,c_fit' + spliturl[1];

                    $('#searchResults').append('<div class="searchResult pure-u-1 pure-u-md-1-3"><img src="' + imageurl + '" class="pure-img searchResult-image"/><div class="searchResult-title"><span>' + data[i].name + '</span></div><div class="searchResult-release"><span>' + data[i].first_release_date + '</span></div></div>');
                }
            }
        });
    });
});