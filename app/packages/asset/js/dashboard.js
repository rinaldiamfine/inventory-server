const availableDay = ["Sun", "Mon", "Tue", "wed", "Thu", "Fri", "Sat"];
const availableYear = ["2018", "2019", "2020", "2021", "2022"]
const avalableMonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
const avalableMonth = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

const ctxLineChart = document.getElementById('lineChart').getContext('2d');
const ctxPieChart = document.getElementById('pieChart').getContext('2d');
const ctxBarChart = document.getElementById('barChart').getContext('2d');

const pieChart = new Chart(ctxPieChart, {
    type: 'doughnut',
    data: {
        labels: avalableMonth,
        datasets: [{
            label: "By Year",
            data: [12, 19, 3, 5, 1, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ]
        }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'right',
        },
        title: {
          display: false,
          text: 'By Month'
        }
      }
    },
});

const lineChart = new Chart(ctxLineChart, {
    type: 'line',
    data: {
        labels: availableYear,
        datasets: [{
            label: "By Year",
            data: [12, 19, 3, 5, 1],
            backgroundColor: [
                // 'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
            ]
        }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'By Year'
        }
      }
    },
});

const barChart = new Chart(ctxBarChart, {
    type: 'bar',
    data: {
        labels: availableDay,
        datasets: [{
            label: 'By Day',
            data: [12, 19, 3, 5, 2, 3, 5],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                // 'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)',
                // 'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});