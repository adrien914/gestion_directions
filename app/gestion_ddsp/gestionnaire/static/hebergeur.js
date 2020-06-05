function modifier_hebergeur(id, direction=null, csrf_token){
    nom = document.getElementById("hebergeur_nom" + id).value
    prenom = document.getElementById("hebergeur_prenom" + id).value
    email = document.getElementById("hebergeur_email" + id).value
    telephone = document.getElementById("hebergeur_tel" + id).value
    autres = document.getElementById("hebergeur_autres" + id).value
    console.log(direction)
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
            console.log(data)
        },
        error: function (error) {
            console.log(error)
        }
    })
}