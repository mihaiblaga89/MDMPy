function showNotification(message) {

    var notification = new NotificationFx({
        message : '<div class="ns-thumb"><img src="/static/images/favico.png"/></div><div class="ns-content"><p>' + message + '</p></div>',
        layout : 'other',
        ttl : 4000,
        effect : 'thumbslider',
        type : 'notice', // notice, warning, error or success
    });
            // show the notification
    notification.show();
}

$(document).ready(function() {

    $(".button-collapse").sideNav();
})
