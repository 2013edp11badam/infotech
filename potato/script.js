$(document).ready(function(){
    var boxwidth = 200
});

$(document).mousemove(function(e){
    $("#window").css({left:e.pageX + 10, top:e.pageY - 50});
});

$(document).click(function(){
    $("#window").width($("#window").width() + 20);
    $("#window").height($("#window").height() + 20);
});
