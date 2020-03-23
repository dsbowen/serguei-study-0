$(document).ready(function(){
    check_responses();
})

function check_responses(){
    response_correct = "true";
    {% for slider_id, correct in slider_info %}
        if ($("#{{ slider_id }}").val() != {{ correct }}){
            response_correct = "false";
        }
    {% endfor %}
    if (response_correct == "true"){
        visibility = "visible";
    }
    else {
        visibility = "hidden";
    }
    document.getElementById('forward-btn').style.visibility = visibility;
}