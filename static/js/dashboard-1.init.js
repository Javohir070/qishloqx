var colors = ["#f1556c"],
    dataColors = $("#total-revenue").data("colors");
dataColors && (colors = dataColors.split(","));
var options = {
        series: [68],
        chart: {
            height: 242,
            type: "radialBar"
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "65%"
                }
            }
        },
        colors: colors,
        labels: ["Revenue"]
    },
    chart = new ApexCharts(document.querySelector("#total-revenue"), options);
chart.render();
colors = ["#1abc9c", "#4a81d4"];
(dataColors = $("#sales-analytics").data("colors")) && (colors = dataColors.split(","));
options = {
    series: [{
        name: "Revenue",
        type: "column",
        data: [440, 505, 414, 671, 227, 413]
    }, {
        name: "Sales",
        type: "line",
        data: [23, 42, 35, 27, 43, 22 ]
    }],
    chart: {
        height: 378,
        type: "line",
        offsetY: 10
    },
    stroke: {
        width: [2, 3]
    },
    plotOptions: {
        bar: {
            columnWidth: "50%"
        }
    },
    colors: colors,
    dataLabels: {
        enabled: !0,
        enabledOnSeries: [1]
    },
    labels: ["01 Jan  2023", "02 Jan  2023", "03 Jan  2023", "04 Jan  2023", "05 Jan  2023", "06 Jan 2023"],
    // labels: ["01 Jan  2023", "02 Yanvar  2023", "03 Fevral  2023", "04 Mart  2023", "05 Aprel  2023", "06 May 2023"],
    xaxis: {
        type: "datetime"
    },
    legend: {
        offsetY: 7
    },
    grid: {
        padding: {
            bottom: 20
        }
    },
    fill: {
        type: "gradient",
        gradient: {
            shade: "light",
            type: "horizontal",
            shadeIntensity: .25,
            gradientToColors: void 0,
            inverseColors: !0,
            opacityFrom: .75,
            opacityTo: .75,
            stops: [0, 0, 0]
        }
    },
    yaxis: [{
        title: {
            text: "Net Revenue"
        }
    }, {
        opposite: !0,
        title: {
            text: "Number of Sales"
        }
    }]
};
(chart = new ApexCharts(document.querySelector("#sales-analytics"), options)).render(), $("#dash-daterange").flatpickr({
    altInput: !0,
    mode: "range",
    altFormat: "F j, y",
    defaultDate: "today"
});