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
            div.empty().show().html("Modifié avec succès").delay(5000).fadeOut(600);
            /* Show the checkmark on the button corresponding to the new state */
            show_active_state(data)
        },
        error: function () {
            /* get the alert div to show the error message in it */
            div = $('#alert_div_hebergement')
            div.addClass("alert-danger")
            div.empty().show().html("Erreur a la modification").delay(5000).fadeOut(300);
        }
    })
}

function show_active_state(data){
    old_button_icon = $('#icon_active_hebergement') // get the button that had the checkmark on it
    old_button_icon.remove() // remove the checkmark from the old button
    new_button = document.getElementById(data.type_hebergement) // get the button which id's corresponds to the new state
    new_button.innerHTML += '<i id="icon_active_hebergement" class="far fa-check-circle faa-check-circle animated faa-4x"></i>' // add the checkmark to the new button
}