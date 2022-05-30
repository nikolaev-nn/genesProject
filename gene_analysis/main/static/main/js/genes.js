function getRandom(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function getInfo(chart) {
    const i = chart.datasetIndex;
    const dataset = coordsDict[i];
    let data = "unknown";
    Object.keys(dataset).forEach(function (key) {
        if (dataset[key]["x"] === chart.parsed.x && dataset[key]["y"] === chart.parsed.y) {
            data = dataset[key];
        }
    })
    return data;
}

const genes = [
    {
        "index": 2669,
        "originalRequest": "Gene1",
        "function": "AHu",
        "labels": 560,
        "xcoord": 3.5681416,
        "ycoord": 17.842126
    }, {
        "index": 2668,
        "originalRequest": "Gene2",
        "function": "Ohh",
        "labels": 55,
        "xcoord": 3.5701516,
        "ycoord": 17.242126
    }, {
        "index": 218,
        "originalRequest": "ADCY3",
        "function": "Catalyzes the formation of the signaling molecule cAMP in response to G-protein signaling. Participates in signaling cascades triggered by odorant receptors via its function in cAMP biosynthesis. Required for the perception of odorants. Required for normal sperm motility and normal male fertility. Plays a role in regulating insulin levels and body fat accumulation in response to a high fat diet.",
        "labels": 56,
        "xcoord": 3.5701516,
        "ycoord": 18.242126
    }, {
        "index": 236,
        "originalRequest": "ADCY6",
        "function": "Catalyzes the formation of the signaling molecule cAMP downstream of G protein-coupled receptors (PubMed:17916776, PubMed:17110384). Functions in signaling cascades downstream of beta-adrenergic receptors in the heart and in vascular smooth muscle cells (PubMed:17916776). Functions in signaling cascades downstream of the vasopressin receptor in the kidney and has a role in renal water reabsorption. Functions in signaling cascades downstream of PTH1R and plays a role in regulating renal phosphate excretion. Functions in signaling cascades downstream of the VIP and SCT receptors in pancreas and contributes to the regulation of pancreatic amylase and fluid secretion (By similarity). Signaling mediates cAMP-dependent activation of protein kinase PKA. This promotes increased phosphorylation of various proteins, including AKT. Plays a role in regulating cardiac sarcoplasmic reticulum Ca(2+) uptake and storage, and is required for normal heart ventricular contractibility. May contribute to normal heart function (By similarity). Mediates vasodilatation after activation of beta-adrenergic receptors by isoproterenol (PubMed:17916776). Contributes to bone cell responses to mechanical stimuli (By similarity).",
        "labels": 56,
        "xcoord": 3.570191,
        "ycoord": 18.242092
    }, {
        "index": 622,
        "originalRequest": "ADCY4",
        "function": "Catalyzes the formation of the signaling molecule cAMP in response to G-protein signaling.",
        "labels": 56,
        "xcoord": 3.5691485,
        "ycoord": 18.238596
    }, {
        "index": 3885,
        "originalRequest": "ADCY4",
        "function": "Catalyzes the formation of the signaling molecule cAMP in response to G-protein signaling.",
        "labels": 56,
        "xcoord": 3.5708616,
        "ycoord": 18.240255
    }, {
        "index": 4642,
        "originalRequest": "ADCY7",
        "function": "Catalyzes the formation of cAMP in response to activation of G protein-coupled receptors (Probable). Functions in signaling cascades activated namely by thrombin and sphingosine 1-phosphate and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G alpha protein with GNA13 (PubMed:23229509, PubMed:18541530). Also, during inflammation, mediates zymosan-induced increase intracellular cAMP, leading to protein kinase A pathway activation in order to modulate innate immune responses through heterotrimeric G proteins G(12\/13) (By similarity). Functions in signaling cascades activated namely by dopamine and C5 alpha chain and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G protein with G beta:gamma complex (PubMed:23842570, PubMed:23229509). Functions, through cAMP response regulation, to keep inflammation under control during bacterial infection by sensing the presence of serum factors, such as the bioactive lysophospholipid (LPA) that regulate LPS-induced TNF-alpha production. However, it is also required for the optimal functions of B and T cells during adaptive immune responses by regulating cAMP synthesis in both B and T cells (By similarity).",
        "labels": 56,
        "xcoord": 3.5702186,
        "ycoord": 18.24316
    }, {
        "index": 5089,
        "originalRequest": "ADCY6",
        "function": "Catalyzes the formation of the signaling molecule cAMP downstream of G protein-coupled receptors (PubMed:17916776, PubMed:17110384). Functions in signaling cascades downstream of beta-adrenergic receptors in the heart and in vascular smooth muscle cells (PubMed:17916776). Functions in signaling cascades downstream of the vasopressin receptor in the kidney and has a role in renal water reabsorption. Functions in signaling cascades downstream of PTH1R and plays a role in regulating renal phosphate excretion. Functions in signaling cascades downstream of the VIP and SCT receptors in pancreas and contributes to the regulation of pancreatic amylase and fluid secretion (By similarity). Signaling mediates cAMP-dependent activation of protein kinase PKA. This promotes increased phosphorylation of various proteins, including AKT. Plays a role in regulating cardiac sarcoplasmic reticulum Ca(2+) uptake and storage, and is required for normal heart ventricular contractibility. May contribute to normal heart function (By similarity). Mediates vasodilatation after activation of beta-adrenergic receptors by isoproterenol (PubMed:17916776). Contributes to bone cell responses to mechanical stimuli (By similarity).",
        "labels": 56,
        "xcoord": 3.5708072,
        "ycoord": 18.244835
    }, {
        "index": 5965,
        "originalRequest": "ADCY4",
        "function": "Catalyzes the formation of the signaling molecule cAMP in response to G-protein signaling.",
        "labels": 56,
        "xcoord": 3.570746,
        "ycoord": 18.236311
    }, {
        "index": 6980,
        "originalRequest": "ADCY7",
        "function": "Catalyzes the formation of cAMP in response to activation of G protein-coupled receptors (Probable). Functions in signaling cascades activated namely by thrombin and sphingosine 1-phosphate and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G alpha protein with GNA13 (PubMed:23229509, PubMed:18541530). Also, during inflammation, mediates zymosan-induced increase intracellular cAMP, leading to protein kinase A pathway activation in order to modulate innate immune responses through heterotrimeric G proteins G(12\/13) (By similarity). Functions in signaling cascades activated namely by dopamine and C5 alpha chain and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G protein with G beta:gamma complex (PubMed:23842570, PubMed:23229509). Functions, through cAMP response regulation, to keep inflammation under control during bacterial infection by sensing the presence of serum factors, such as the bioactive lysophospholipid (LPA) that regulate LPS-induced TNF-alpha production. However, it is also required for the optimal functions of B and T cells during adaptive immune responses by regulating cAMP synthesis in both B and T cells (By similarity).",
        "labels": 56,
        "xcoord": 3.5705428,
        "ycoord": 18.242231
    }, {
        "index": 7566,
        "originalRequest": "ADCY6",
        "function": "Catalyzes the formation of the signaling molecule cAMP downstream of G protein-coupled receptors (PubMed:17916776, PubMed:17110384). Functions in signaling cascades downstream of beta-adrenergic receptors in the heart and in vascular smooth muscle cells (PubMed:17916776). Functions in signaling cascades downstream of the vasopressin receptor in the kidney and has a role in renal water reabsorption. Functions in signaling cascades downstream of PTH1R and plays a role in regulating renal phosphate excretion. Functions in signaling cascades downstream of the VIP and SCT receptors in pancreas and contributes to the regulation of pancreatic amylase and fluid secretion (By similarity). Signaling mediates cAMP-dependent activation of protein kinase PKA. This promotes increased phosphorylation of various proteins, including AKT. Plays a role in regulating cardiac sarcoplasmic reticulum Ca(2+) uptake and storage, and is required for normal heart ventricular contractibility. May contribute to normal heart function (By similarity). Mediates vasodilatation after activation of beta-adrenergic receptors by isoproterenol (PubMed:17916776). Contributes to bone cell responses to mechanical stimuli (By similarity).",
        "labels": 56,
        "xcoord": 3.5687544,
        "ycoord": 18.243196
    }, {
        "index": 9009,
        "originalRequest": "ADCY7",
        "function": "Catalyzes the formation of cAMP in response to activation of G protein-coupled receptors (Probable). Functions in signaling cascades activated namely by thrombin and sphingosine 1-phosphate and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G alpha protein with GNA13 (PubMed:23229509, PubMed:18541530). Also, during inflammation, mediates zymosan-induced increase intracellular cAMP, leading to protein kinase A pathway activation in order to modulate innate immune responses through heterotrimeric G proteins G(12\/13) (By similarity). Functions in signaling cascades activated namely by dopamine and C5 alpha chain and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G protein with G beta:gamma complex (PubMed:23842570, PubMed:23229509). Functions, through cAMP response regulation, to keep inflammation under control during bacterial infection by sensing the presence of serum factors, such as the bioactive lysophospholipid (LPA) that regulate LPS-induced TNF-alpha production. However, it is also required for the optimal functions of B and T cells during adaptive immune responses by regulating cAMP synthesis in both B and T cells (By similarity).",
        "labels": 56,
        "xcoord": 3.5705848,
        "ycoord": 18.242916
    }, {
        "index": 9820,
        "originalRequest": "ADCY9",
        "function": "Adenylyl cyclase that catalyzes the formation of the signaling molecule cAMP in response to activation of G protein-coupled receptors (PubMed:9628827, PubMed:12972952, PubMed:15879435, PubMed:10987815). Contributes to signaling cascades activated by CRH (corticotropin-releasing factor), corticosteroids and beta-adrenergic receptors (PubMed:9628827).",
        "labels": 56,
        "xcoord": 3.56659,
        "ycoord": 18.240568
    }, {
        "index": 11322,
        "originalRequest": "ADCY7",
        "function": "Catalyzes the formation of cAMP in response to activation of G protein-coupled receptors (Probable). Functions in signaling cascades activated namely by thrombin and sphingosine 1-phosphate and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G alpha protein with GNA13 (PubMed:23229509, PubMed:18541530). Also, during inflammation, mediates zymosan-induced increase intracellular cAMP, leading to protein kinase A pathway activation in order to modulate innate immune responses through heterotrimeric G proteins G(12\/13) (By similarity). Functions in signaling cascades activated namely by dopamine and C5 alpha chain and mediates regulation of cAMP synthesis through synergistic action of the stimulatory G protein with G beta:gamma complex (PubMed:23842570, PubMed:23229509). Functions, through cAMP response regulation, to keep inflammation under control during bacterial infection by sensing the presence of serum factors, such as the bioactive lysophospholipid (LPA) that regulate LPS-induced TNF-alpha production. However, it is also required for the optimal functions of B and T cells during adaptive immune responses by regulating cAMP synthesis in both B and T cells (By similarity).",
        "labels": 56,
        "xcoord": 3.5701869,
        "ycoord": 18.24269
    }];
let datasets = [];
let coordsDict = {};
const indexes = [55, 56, 560];

for (let gene of genes) {
    const x = gene['xcoord'];
    const y = gene['ycoord'];
    const title = gene['originalRequest'];
    const description = gene['function'];

    let index = 0;
    for (let i of indexes) {
        if (i === gene["labels"]) {
            if (coordsDict[index] === undefined) {
                coordsDict[index] = [{x, y, title, description}]
            } else {
                coordsDict[index].push({
                    x, y, title, description
                });
            }
        }
        index++;
    }
}

Object.keys(coordsDict).forEach(function (key) {
    datasets.push(
        {
            datasetIndex: parseInt(key),
            pointRadius: 4,
            pointBackgroundColor: `rgb(${getRandom(0, 255)}, ${getRandom(0, 255)}, ${getRandom(0, 255)})`,
            borderColor: "black",
            data: coordsDict[key],

        }
    );
});

const ctx = document.getElementById("myChart");
let config = {
    type: "scatter",
    data: {
        datasets: datasets
    },
    options: {
        animation: false,
        plugins: {
            legend: {display: false},
            tooltip: {
                callbacks: {
                    title: function (chart) {
                        return getInfo(chart[0])["title"];
                    },
                    label: function (chart) {
                        return getInfo(chart)["description"]
                    },
                },
            },
            zoom: {
                zoom: {
                    wheel: {
                        enabled: true,
                    },
                    pinch: {
                        enabled: true
                    },
                }
            },
        },
        scales: {
            x: {
                display: false
            },
            y: {
                display: false
            }
        }
    },
}

const myChart = new Chart(
    ctx,
    config,
);

function clickHandler(click) {
    const points = myChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points.length !== 0) {
        const newChart = {datasetIndex: points[0].datasetIndex, parsed: points[0].element['$context'].parsed}
        const newData = getInfo(newChart);
        document.getElementById("title").textContent = newData['title'];
        document.getElementById("description").textContent = newData['description'];
    }
}

ctx.onclick = clickHandler;