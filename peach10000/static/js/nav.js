function navTitleColor(blockName) {
    var titleObj = document.getElementById('nav_title');
    if (blockName == "#blockB") {
        titleObj.style.color = "#FFFFFF";
    }
    return
}

function changeTitleColor(color) {
    // 0 : #643200, 1 :　#FFFFFF
    let titleButton = document.getElementById('nav_title');
    if (color == 0) {
        titleButton.style.color = '#643200';
    } else if (color == 1) {
        titleButton.style.color = '#FFFFFF';
    }
}