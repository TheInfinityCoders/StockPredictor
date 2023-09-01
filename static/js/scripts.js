const ctx = document.getElementById("myChart");

const company = ctx.dataset.company;

var labels = ctx.dataset.labels.split(",");
var close_data = ctx.dataset.close.split(",");

new Chart(ctx, {
    type: "line",
    data: {
        labels: labels,
        datasets: [
            {
                label: `${company}`,
                data: close_data,
                borderWidth: 2.5,
                fill: true,
            },
        ],
    },
    options: {
        elements: {
            point: {
                radius: 1.5,
            },
        },
        layout: {
            padding: {
                bottom: 20,
                right: 15,
            },
        },
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: "Closed Price (USD)",
                    color: "black",
                    font: {
                        size: 14
                    }
                },
                ticks: {
                    color: "black",
                    font: {
                        size: 14
                    }
                },
                grid: {
                    color: "rgba(0, 0, 0, 0.3)",
                },
                border: {
                    color: "black",
                },
            },
            x: {
                ticks: {
                    color: "black",
                    font: {
                        size: 14
                    },
                    display: false,
                },
                grid: {
                    display: false,
                },
                border: {
                    color: "black",
                }
            },
        },
        plugins: {
            legend: {
                display: false,
            },
            title: {
                display: true,
                text: company,
                color: "black",
                font: {
                    size: 20,
                    weight: "bold",
                },
                padding: {
                    bottom: 30,
                    top: 10,
                },
            },
        },
    },
});