function modifier_hebergeur(id, direction, csrf_token){
    nom = document.getElementById("hebergeur_nom" + id).value
    prenom = document.getElementById("hebergeur_prenom" + id).value
    email = document.getElementById("hebergeur_email" + id).value
    telephone = document.getElementById("hebergeur_tel" + id).value
    autres = document.getElementById("hebergeur_autres" + id).value
    data = {
        nom: nom,
        prenom: prenom,
        email: email,
        telephone: telephone,
        autres: autres,
        hebergeur_id: id,
        csrfmiddlewaretoken: csrf_token,
        direction: direction
    }
    $.ajax({
        url: "/create_or_modify_hebergeur/",
        data: data,
        type: "POST",
        success: function (data) {
            $(`#hebergeur-modal${id}`).modal('hide')
            if (id.toString() !== "_create")
                document.getElementById(`hebergeur_edit_button${id}`).innerHTML = email
            else
                add_hebergeur_button(data.hebergeur_data, csrf_token)
        },
        error: function (response) {
            $(`#hebergeur-modal${id}`).modal('hide')
            div = $('#alert_div_hebergeurs')
            div.addClass("alert-danger")
            if (response.status === 401)
                div.empty().html("Vous n'avez pas la permission de modifier celà").fadeIn(1000).delay(3000).fadeOut(600);
            else
                div.empty().html("Erreur a la modification").fadeIn(1000).delay(3000).fadeOut(600);
        }
    })
}

function delete_hebergeur(id, csrf_token) {
    $.ajax({
        url: '/delete_hebergeur/',
        type: 'POST',
        data: {id: id, csrfmiddlewaretoken: csrf_token},
        success: function () {
            edit_button = $(`#hebergeur_edit_button${id}`)
            delete_button = $(`#hebergeur_delete_button${id}`)
            edit_button.remove()
            delete_button.remove()
        }
    })
}

function add_hebergeur_button(hebergeur, csrf_token) {
    var html = `
    <button id="hebergeur_edit_button${hebergeur.id}"
            type="button" class="btn btn-info mt-1 mb-1 ml-auto col-5 zoom" data-toggle="modal"
            data-target="#hebergeur-modal${hebergeur.id}">${hebergeur.email}</button>
    <button id="hebergeur_delete_button${hebergeur.id}"
            onclick="delete_hebergeur(${hebergeur.id}, '${csrf_token}')"
            type="button" class="btn btn-danger mt-1 mr-auto mb-1 zoom faa-parent animated-hover"><i class="far fa-trash-alt faa-trash-alt"></i></button>
    <div class="modal fade" id="hebergeur-modal${hebergeur.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Infos sur ${hebergeur.email}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="hebergeur_nom${hebergeur.id}" class="col-form-label">Nom:</label>
                <input type="text" class="form-control" id="hebergeur_nom${hebergeur.id}" value="${hebergeur.nom }">
              </div>
              <div class="form-group">
                <label for="hebergeur_prenom${hebergeur.id}" class="col-form-label">Prénom:</label>
                <input type="text" class="form-control" id="hebergeur_prenom${hebergeur.id}" value="${hebergeur.prenom}">
              </div>
                <div class="form-group">
                <label for="hebergeur_email${hebergeur.id}" class="col-form-label">Email:</label>
                <input type="text" class="form-control" id="hebergeur_email${hebergeur.id}" value="${hebergeur.email}">
              </div>
                <div class="form-group">
                <label for="hebergeur_tel${hebergeur.id}" class="col-form-label">Téléphone:</label>
                <input type="text" class="form-control" id="hebergeur_tel${hebergeur.id}" value="${hebergeur.telephone}">
              </div>
                <div class="form-group">
                <label for="hebergeur_autres${hebergeur.id}" class="col-form-label">Autres:</label>
                <textarea class="form-control" id="hebergeur_autres${hebergeur.id}" >${hebergeur.autres}</textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
            <button type="button" class="btn btn-primary" onclick="modifier_hebergeur(${hebergeur.id}, '', '${csrf_token}')">Modifier</button>
          </div>
        </div>
      </div>
    </div>
    `
    $("#hebergeurs-buttons").prepend(html)
}