// Setup
const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const data = {
  labels: labels,
  datasets: [{
    label: 'Monthly Sales',
    data: [1200, 1350, 980, 1450, 1600, 1780, 1650, 1720, 1580, 1800, 1900, 2100],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};


// Config
const config = {
  type: 'line',
  data,
  options: {}
};


var myChart = new Chart(
    document.getElementById('monthly-sales'),
    config
  );

// Pie Chart
const data1 = {
  labels: [
    'Red',
    'Blue',
    'Yellow'
  ],
  datasets: [{
    label: 'My First Dataset',
    data: [300, 50, 100],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
};

const config1 = {
  type: 'doughnut',
  data: data,
};