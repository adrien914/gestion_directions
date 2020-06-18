function set_listener_url(csrf_token) {
     let typingTimer;                //timer identifier
     let doneTypingInterval = 1300;  //time in ms, 5 second for example
     let $input = $('#url_site');

     //on keyup, start the countdown
     $input.on('keyup', function () {
         clearTimeout(typingTimer);
         typingTimer = setTimeout(function () { doneTypingUrl(csrf_token) }, doneTypingInterval);
     });

     //on keydown, clear the countdown
     $input.on('keydown', function () {
         clearTimeout(typingTimer);
     });
 }

//user is "finished typing," do something
function doneTypingUrl (csrf_token) {
    const text = document.getElementById('url_site').value
    const direction_id = document.getElementById('direction-id').value
    $.ajax({
        type: "POST",
        url: "/save_url/",
        data: {
            text: text,
            direction_id: direction_id,
            csrfmiddlewaretoken: csrf_token
        },
        success: function (data) {
            div = $('#alert_div_url')
            div.addClass("alert-success")
            div.empty().html("Sauvegardé avec succès").fadeIn(1000).delay(3000).fadeOut(600);
        },
        error: function (response) {
            /* get the alert div to show the error message in it */
            div = $('#alert_div_url')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function set_listener_version(csrf_token) {
     let typingTimer;                //timer identifier
     let doneTypingInterval = 1300;  //time in ms, 5 second for example
     let $input = $('#version_joomla');

     //on keyup, start the countdown
     $input.on('keyup', function () {
         clearTimeout(typingTimer);
         typingTimer = setTimeout(function () { doneTypingVersion(csrf_token) }, doneTypingInterval);
     });

     //on keydown, clear the countdown
     $input.on('keydown', function () {
         clearTimeout(typingTimer);
     });
 }

//user is "finished typing," do something
function doneTypingVersion (csrf_token) {
    const text = document.getElementById('version_joomla').value
    const direction_id = document.getElementById('direction-id').value
    $.ajax({
        type: "POST",
        url: "/save_version/",
        data: {
            text: text,
            direction_id: direction_id,
            csrfmiddlewaretoken: csrf_token
        },
        success: function (data) {
            div = $('#alert_div_version')
            div.addClass("alert-success")
            div.empty().html("Sauvegardé avec succès").fadeIn(1000).delay(3000).fadeOut(600);
        },
        error: function (response) {
            /* get the alert div to show the error message in it */
            div = $('#alert_div_version')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}