function modifier_deplacement(id, csrf_token){
    destination = document.getElementById("deplacement_destination" + id).value
    date = document.getElementById("deplacement_date" + id).value
    commentaires = document.getElementById("deplacement_commentaires" + id).value
    data = {
        destination: destination,
        date: date,
        commentaires: commentaires,
        deplacement_id: id,
        csrfmiddlewaretoken: csrf_token,
    }
    console.log("test")
    $.ajax({
        url: "/create_or_modify_deplacement/",
        data: data,
        type: "POST",
        success: function (data) {
            $(`#deplacement-modal${id}`).modal('hide')
            if (id.toString() !== "_create")
                document.getElementById(`deplacement_edit_button${id}`).innerHTML = destination + " à " + date
            else
                add_deplacement_button(data.deplacement_data, csrf_token)
        },
        error: function (response) {
            $(`#deplacement-modal${id}`).modal('hide')
            div = $('#alert_div_deplacement')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function delete_deplacement(id, csrf_token) {
    $.ajax({
        url: '/delete_deplacement/',
        type: 'POST',
        data: {id: id, csrfmiddlewaretoken: csrf_token},
        success: function () {
            edit_button = $(`#deplacement_edit_button${id}`)
            delete_button = $(`#deplacement_delete_button${id}`)
            edit_button.remove()
            delete_button.remove()
        },
        error: function (response) {
            div = $('#alert_div_deplacement')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function add_deplacement_button(deplacement, csrf_token) {
    var html = `
    <button id="deplacement_edit_button${deplacement.id}"
            type="button" class="btn btn-info mt-1 mb-1 ml-auto col-5 zoom" data-toggle="modal"
            data-target="#deplacement-modal${deplacement.id}">${deplacement.destination} le ${deplacement.date}</button>
    <button id="deplacement_delete_button${deplacement.id}"
            onclick="delete_deplacement(${deplacement.id}, '${csrf_token}')"
            type="button" class="btn btn-danger mt-1 mr-auto mb-1 zoom faa-parent animated-hover"><i class="far fa-trash-alt faa-trash-alt"></i></button>
    <div class="modal fade" id="deplacement-modal${deplacement.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Infos sur le déplacement</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="deplacement_destination${deplacement.id}" class="col-form-label">Nom:</label>
                <input type="text" class="form-control" id="deplacement_destination${deplacement.id}" value="${deplacement.destination }">
              </div>
              <div class="form-group">
                <label for="deplacement_date${deplacement.id}" class="col-form-label">Prénom:</label>
                <input type="text" class="form-control" id="deplacement_date${deplacement.id}" value="${deplacement.date}">
              </div>
                <div class="form-group">
                <label for="deplacement_commentaire${deplacement.id}" class="col-form-label">Autres:</label>
                <textarea class="form-control" id="deplacement_commentaire${deplacement.id}" >${deplacement.commentaires}</textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
            <button type="button" class="btn btn-primary" onclick="modifier_deplacement(${deplacement.id}, '${csrf_token}')">Modifier</button>
          </div>
        </div>
      </div>
    </div>
    `
    $("#deplacements-buttons").prepend(html)
}