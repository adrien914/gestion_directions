 function set_listener_stagiaire(csrf_token) {
     let typingTimer;                //timer identifier
     let doneTypingInterval = 500;  //time in ms, 5 second for example
     let $input = $('#stagiaire-input');

     //on keyup, start the countdown
     $input.on('keyup', function () {
         clearTimeout(typingTimer);
         typingTimer = setTimeout(function () { doneTyping(csrf_token) }, doneTypingInterval);
     });

     //on keydown, clear the countdown
     $input.on('keydown', function () {
         clearTimeout(typingTimer);
     });
 }

//user is "finished typing," do something
function doneTyping (csrf_token) {
    const text = document.getElementById('stagiaire-input').value
    const direction_id = document.getElementById('direction-id').value
    $.ajax({
        type: "POST",
        url: "/save_stagiaire/",
        data: {
            text: text,
            direction_id: direction_id,
            csrfmiddlewaretoken: csrf_token
        },
        success: function (data) {
            div = $('#alert_div_stagiaire')
            div.addClass("alert-success")
            div.empty().html("Sauvegardé avec succès").fadeIn(1000).delay(3000).fadeOut(600);
        },
        error: function (response) {
            div = $('#alert_div_stagiaire')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        },
    })
}