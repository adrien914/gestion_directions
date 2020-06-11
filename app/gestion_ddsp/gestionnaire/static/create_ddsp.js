function create_ddsp(csrf_token){
    const name = document.getElementById('nom_ddsp').value
    $.ajax({
        type: "POST",
        url: "/create_ddsp/",
        data: {name: name, csrfmiddlewaretoken: csrf_token},
        success: function () {
            location.href = `/gestion/${name}`
        }
    })
}