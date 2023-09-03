//Chart Drawing

const ctx = document.getElementById("myChart");

const company = ctx.dataset.company;

var labels = ctx.dataset.labels.split(",");
var close_data = ctx.dataset.close.split(",");
var range = ctx.dataset.range;
console.log(range);

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
                    text: "Closing Price (USD)",
                    color: "black",
                    font: {
                        size: 16
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
                title: {
                    display: true,
                    text: range,
                    color: "black",
                    font: {
                        size: 16
                    }
                },
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

// Date Input defaults to today
document.getElementById("date-input").value = new Date().toISOString().split("T")[0]

// Navbar dropdown list
function displayMenu() {
    $("#dropdown-menu").toggleClass("hidden");
    $("#dropdown-menu").toggleClass("block");
}

function enteredMenu() {
    let menu = $("#dropdown-menu");

    menu.on("mouseleave", () => {
        menu.toggleClass("hidden");
        menu.toggleClass("block");
    });
}