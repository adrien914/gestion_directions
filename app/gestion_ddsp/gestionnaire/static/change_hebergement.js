function change_hebergement(type_hebergement, direction, csrf_token) {
    /*
    *   new_state = the new state for the direction
    *   direction = the name of the direction we're on
    */
    $.ajax({
        url: "/change_hebergement/",
        type: "POST",
        data: {
            type_hebergement: type_hebergement,
            direction: direction,
            csrfmiddlewaretoken: csrf_token
        },
        success: function (data) {
            /* get the alert div to show the success message in it */
            div = $('#alert_div_hebergement')
            div.addClass("alert-success")
            div.empty().html("Modifié avec succès").fadeIn(1000).delay(3000).fadeOut(600);
            /* Show the checkmark on the button corresponding to the new state */
            show_active_state(data)
        },
        error: function (response) {
            /* get the alert div to show the error message in it */
            div = $('#alert_div_hebergement')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function show_active_state(data){
    old_button_icon = $('#icon_active_hebergement') // get the button that had the checkmark on it
    old_button_icon.remove() // remove the checkmark from the old button
    new_button = document.getElementById(data.type_hebergement) // get the button which id's corresponds to the new state
    new_button.innerHTML += '<i id="icon_active_hebergement" class="far fa-check-circle faa-check-circle animated faa-4x"></i>' // add the checkmark to the new button
}