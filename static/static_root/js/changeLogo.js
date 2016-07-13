var $imgs = $(".logoImage").find("img"),
    i = 0;

function changeImage(){
    var next = (++i % $imgs.length);
    $($imgs.get(next - 1)).fadeOut(0);
    $($imgs.get(next)).fadeIn(0);
}
var interval = setInterval(changeImage, 150);