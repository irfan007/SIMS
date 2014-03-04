$(document).ready(function()
{

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

jQuery.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

 
$("table").delegate(".detail","click", function(e)
{
    // e.preventDefault();
    var eid = this.id;

    if(eid != "")
    {
    $.ajax({
            cache: false,
            url: "/student/detail/?eid="+eid+"/",
            data: {'eid':eid} ,
            success: function(data){
              
                    // alert(data);
                    $( ".modal-body").html("");
                    $( ".modal-body").append( data );
                    },
            });
    }
});

$(".more").on("click", function(e)
    {
        var query = $("#query").val()
        var offset = $("#offset").val()
        if(offset != "")
        {
        $.ajax({
                type: "POST",
                url: "/student/search/name/",
                data: {'sname': query, 'offset': offset},
                success: function(data){
                        alert(data)
                        if (data !== ""){
                            $("#offset").val(parseInt(offset)+5)
                            $( "tbody").append( data );
                        }
                        else {
                            alert("No More Result");
                        }
                        },
                });
        }
    });
});