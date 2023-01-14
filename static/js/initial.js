$(document).ready(function() {
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    if (windowWidth < 775) {
        var imgg = document.querySelector('.content_img');
        imgg.style = "max-height:90px";
        imgg.style = "max-width:90px";
    }

})