function replaceForm(e) {
    if (e.keyCode === 13) {
        // document.getElementById("wrapper").hidden = true
        document.getElementById("loader").hidden = false
    }
}

$(document).ready(function () {
    $('#search').keypress(function (e) {
        replaceForm(e)
    });
    $('#randomSearch').keypress(function (e) {
        replaceForm(e)
    });
});
