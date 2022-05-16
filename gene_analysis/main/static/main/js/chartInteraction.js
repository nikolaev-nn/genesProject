$('#downloadPdf').click(function (event) {
    const reportPageHeight = $('#reportPage').innerHeight();
    const reportPageWidth = $('#reportPage').innerWidth();

    let pdfCanvas = $('<canvas />').attr({
        id: "canvaspdf",
        width: reportPageWidth,
        height: reportPageHeight
    });

    let pdfctx = $(pdfCanvas)[0].getContext('2d');

    let newCanvas = document.getElementById("myChart");
    let canvasHeight = $(newCanvas).innerHeight();
    let canvasWidth = $(newCanvas).innerWidth();

    pdfctx.drawImage($(newCanvas)[0], 400, 30, canvasWidth, canvasHeight);
    let pdf = new jsPDF('l', 'pt', [reportPageWidth, reportPageHeight]);

    pdf.addImage($(pdfCanvas)[0], 'PNG', 0, 0);

    pdf.save('filename.pdf');
});


$(function () {
    $('#saveToFavourites').submit(function (e) {
        alert('a')
    })
})


function saveRequestData(frm, data, type) {
    $.ajax({
        url: frm.attr("action"),
        type: frm.attr("method"),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        success: function (data) {
            alert(data.message)
        }
    });
}