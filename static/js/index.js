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
    fetch('./get_info', {
            method: 'post',
            body: positionId,
        })
        .then(response => {
            return response.json();
        })
        .then(json => {
            var fixedBlock = document.querySelector('.fixedBlock');
            fixedBlock.style.width = "70%";
            var slideBlock = document.querySelector('.slideBlock');
            slideBlock.style.width = "29%";
            JSON.parse(JSON.stringify(json), function(key, value) {
                var slide_title = document.querySelector('.sildeTitle');
                var slide_phone = document.querySelector('#slidePhone');
                var slide_web = document.querySelector('#slideWeb');
                if (key == 'store_name') slide_title.textContent = value;
                if (key == 'store_phone') slide_phone.textContent = value;
                if (key == 'store_web') slide_web.textContent = value;

            })
            return json
        })
}