$('#downloadPdf').click(function (event) {
    const reportPageHeight = $('#reportPage').innerHeight() + 30;
    const reportPageWidth = $('#reportPage').innerWidth();

    let pdfCanvas = $('<canvas />').attr({
        id: "myChart",
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
    console.log(1)
    window.open(URL.createObjectURL(pdf.output("blob")))
});