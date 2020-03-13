function adjustHeight(el){
    el.style.height = (el.scrollHeight > el.clientHeight) ? (el.scrollHeight)+"px" : "60px";
}

$.post("{{url_for('stories', stories_id=story._id)}}", function(data){

    $("#myModal").html(data).fadeIn();

});