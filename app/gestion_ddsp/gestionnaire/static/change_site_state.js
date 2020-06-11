function change_site_state(new_state, direction, csrf_token) {
    /*
    *   new_state = the new state for the direction
    *   direction = the name of the direction we're on
    */
    $.ajax({
        url: "/change_site_state/",
        type: "POST",
        data: {
            state: new_state,
            direction: direction,
            csrfmiddlewaretoken: csrf_token
        },
        success: function (data) {
            /* get the alert div to show the success message in it */
            div = $('#alert_div_etat_site')
            div.addClass("alert-success")
            div.empty().html("Modifié avec succès").fadeIn(1000).delay(3000).fadeOut(600);
            /* Show the checkmark on the button corresponding to the new state */
            show_active_state_site(data)
        },
        error: function () {
            /* get the alert div to show the error message in it */
            div = $('#alert_div_etat_site')
            div.addClass("alert-danger")
            div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function show_active_state_site(data){
    old_button_icon = $('#icon_active_site_state') // get the button that had the checkmark on it
    old_button_icon.remove() // remove the checkmark from the old button
    new_button = document.getElementById(data.new_state) // get the button which id's corresponds to the new state
    new_button.innerHTML += '<i id="icon_active_site_state" class="far fa-check-circle faa-check-circle animated faa-4x"></i>' // add the checkmark to the new button
}