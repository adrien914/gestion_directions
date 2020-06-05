function modifier_contact(id, direction, csrf_token){
    nom = document.getElementById("contact_nom" + id).value
    prenom = document.getElementById("contact_prenom" + id).value
    email = document.getElementById("contact_email" + id).value
    telephone = document.getElementById("contact_tel" + id).value
    autres = document.getElementById("contact_autres" + id).value
    data = {
        nom: nom,
        prenom: prenom,
        email: email,
        telephone: telephone,
        autres: autres,
        contact_id: id,
        csrfmiddlewaretoken: csrf_token,
        direction: direction
    }
    $.ajax({
        url: "/create_or_modify_contact/",
        data: data,
        type: "POST",
        success: function (data) {
            $(`#contact-modal${id}`).modal('hide')
            if (id.toString() !== "_create")
                document.getElementById(`contact_edit_button${id}`).innerHTML = email
            else
                add_contact_button(data.contact_data, csrf_token)
        },
        error: function (error) {
            console.log("error = " + error)
        }
    })
}

function delete_contact(id, csrf_token) {
    $.ajax({
        url: '/delete_contact/',
        type: 'POST',
        data: {id: id, csrfmiddlewaretoken: csrf_token},
        success: function () {
            edit_button = $(`#contact_edit_button${id}`)
            delete_button = $(`#contact_delete_button${id}`)
            edit_button.remove()
            delete_button.remove()
        }
    })
}

function add_contact_button(contact, csrf_token) {
    var html = `
    <button id="contact_edit_button${contact.id}"
            type="button" class="btn btn-info mt-1 mb-1 ml-auto col-5 zoom" data-toggle="modal"
            data-target="#contact-modal${contact.id}">${contact.email}</button>
    <button id="contact_delete_button${contact.id}"
            onclick="delete_contact(${contact.id}, '${csrf_token}')"
            type="button" class="btn btn-danger mt-1 mr-auto mb-1 zoom faa-parent animated-hover"><i class="far fa-trash-alt faa-trash-alt"></i></button>
    <div class="modal fade" id="contact-modal${contact.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Infos sur ${contact.email}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="contact_nom${contact.id}" class="col-form-label">Nom:</label>
                <input type="text" class="form-control" id="contact_nom${contact.id}" value="${contact.nom }">
              </div>
              <div class="form-group">
                <label for="contact_prenom${contact.id}" class="col-form-label">Prénom:</label>
                <input type="text" class="form-control" id="contact_prenom${contact.id}" value="${contact.prenom}">
              </div>
                <div class="form-group">
                <label for="contact_email${contact.id}" class="col-form-label">Email:</label>
                <input type="text" class="form-control" id="contact_email${contact.id}" value="${contact.email}">
              </div>
                <div class="form-group">
                <label for="contact_tel${contact.id}" class="col-form-label">Téléphone:</label>
                <input type="text" class="form-control" id="contact_tel${contact.id}" value="${contact.telephone}">
              </div>
                <div class="form-group">
                <label for="contact_autres${contact.id}" class="col-form-label">Autres:</label>
                <textarea class="form-control" id="contact_autres${contact.id}" >${contact.autres}</textarea>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
            <button type="button" class="btn btn-primary" onclick="modifier_contact(${contact.id}, '', '${csrf_token}')">Modifier</button>
          </div>
        </div>
      </div>
    </div>
    `
    $("#contacts-buttons").prepend(html)
}