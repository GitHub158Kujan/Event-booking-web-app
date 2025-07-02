 const toggleBtn = document.getElementById('toggle-btn');
  const sidebar = document.getElementById('sidebar');

  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
  });

 setTimeout(function() {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
      // Use Bootstrap's fade-out class
      alert.classList.remove('show');
      alert.classList.add('fade');
      
      // Fully remove after fade animation (500ms)
      setTimeout(function() {
        alert.remove();
      }, 500);
    });
  }, 3000);

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
const data = {
  labels: labels,
  datasets: [{
    label: 'Monthly Sales',
    data: [1200, 950, 1340, 1600, 1450, 1780, 2100, 1950, 1700, 1550, 1400, 1250],
    fill: false,
    borderColor: 'rgb(245, 123, 8)',
    tension: 0.1
  }]
};

const config = {
  type: 'line',
  data: data,
   options: {
      plugins: {
        legend: {
          display: false,
        }
      }
    }
};

const myChart = new Chart(
    document.getElementById('salesChart'),
    config
  );


// donut chart

const data_genre = {
  labels: [
    'Music',
    'Sports',
    'Art &  Theatre'
  ],
  datasets: [{
    label: 'Sales',
    labels:'Genre',
    data: [3201, 5009, 1303],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
};


 const config_genre = {
    type: 'doughnut',
    data: data_genre,
    options: {
      plugins: {
        legend: {
          position: 'right',
        }
        

      }
    }
  };

const myChart_1 = new Chart(
    document.getElementById('genreChart'),
    config_genre
  );