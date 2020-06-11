function remove_ddsp(direction, csrf_token){
    $.ajax({
        type: "POST",
        url: "/remove_ddsp/",
        data: {name: direction, csrfmiddlewaretoken: csrf_token},
        success: function () {
            location.href = `/gestion/`
        }
    })
}