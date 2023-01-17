function bbing() {
    const svgImage = document.getElementById("svg5");
    var zoom = parseInt(svgImage.style.zoom, 10) || 100;
    console.log(zoom);
    zoom += event.wheelDelta / 12;
    if (1600 * zoom / 100 <= window.innerWidth * 0.70)
        zoom -= event.wheelDelta / 12;

    if (zoom > 0) svgImage.style.zoom = zoom + "%";
    return false;
}

function zoomingByButton(num) {
    const svgImage = document.getElementById("svg5");
    const svgContainer = document.getElementsByClassName("mapp");
    var zoom = parseInt(svgImage.style.zoom, 10) || 100;
    console.log(zoom);
    zoom += num
    if (1600 * zoom / 100 <= window.innerWidth * 0.70)
        zoom -= num

    if (zoom > 0) svgImage.style.zoom = zoom + "%";
    return false;
}

function slideOut() {
    var fixedBlock = document.querySelector('.fixedBlock');
    fixedBlock.style.width = "100%";
    var slideBlock = document.querySelector('.slideBlock');
    slideBlock.style.width = "0%";
}

function slideIn(positionId) {
    if (positionId === undefined) {
        var slide_title = document.querySelector('.sildeTitle');
        var slide_phone = document.querySelector('#slidePhone');
        var slide_web = document.querySelector('#slideWeb');
        var slide_addr = document.querySelector('#slideAddr');
        var slide_time = document.querySelector('#slideTime');
        var slide_intro = document.querySelector("#slideIntro");
        slide_title.textContent = "尚未收錄";
        slide_phone.textContent = "尚未收錄";
        slide_web.textContent = "尚未收錄";
        slide_addr.textContent = "尚未收錄";
        slide_time.textContent = "尚未收錄";
        slide_web.href = "#blockC";
        slide_intro.href = "#blockC";

        var imgBlock = document.querySelector('#slideTitleImg');
        imgBlock.src = '#';
    }
    fetch('./get_info', {
            method: 'post',
            body: positionId,
        })
        .then(response => {
            return response.json();
        })
        .then(json => {

            JSON.parse(JSON.stringify(json), function(key, value) {
                var slide_title = document.querySelector('.sildeTitle');
                var slide_phone = document.querySelector('#slidePhone');
                var slide_web = document.querySelector('#slideWeb');
                var slide_addr = document.querySelector('#slideAddr');
                var slide_time = document.querySelector('#slideTime');
                var slide_intro = document.querySelector("#slideIntro");

                if (key == 'store_name') slide_title.textContent = value;
                if (key == 'store_phone') slide_phone.textContent = value;
                if (key == 'store_time') slide_time.textContent = value;
                if (key == 'store_addr') slide_addr.textContent = value;
                if (key == 'store_web') {
                    slide_web.textContent = value;
                    slide_web.href = value;
                }
                slide_intro.href = "".concat("/post/", positionId);
            })
            return json
        })


    fetch('./getStoreTitleImg', {
            method: 'post',
            body: positionId,
        })
        .then(response => {
            return response.text();
        })
        .then(text => {
            var imgBlock = document.querySelector('#slideTitleImg');
            imgBlock.src = text;

        })
    var fixedBlock = document.querySelector('.fixedBlock');
    fixedBlock.style.width = "70%";
    var slideBlock = document.querySelector('.slideBlock');
    slideBlock.style.width = "29%";
}