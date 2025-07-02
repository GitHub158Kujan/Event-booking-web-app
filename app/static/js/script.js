document.addEventListener("DOMContentLoaded", function () {
    const plus = document.querySelector(".plus");
    const minus = document.querySelector(".minus");
    const num = document.querySelector(".num");
    const ticketsInput = document.getElementById("ticketsInput");
    const totalPriceDisplay = document.getElementById("totalPrice");

    const pricePerTicket = parseFloat(totalPriceDisplay.textContent) || 0;
    let ticketCount = 1;

    function updateDisplay() {
        num.innerText = ticketCount.toString().padStart(2, "0");
        ticketsInput.value = ticketCount;
        const total = (ticketCount * pricePerTicket).toFixed(2);
        totalPriceDisplay.textContent = total;
    }

    if (plus && minus && num && ticketsInput && totalPriceDisplay) {
        plus.addEventListener("click", () => {
            ticketCount++;
            updateDisplay();
        });

        minus.addEventListener("click", () => {
            if (ticketCount > 1) {
                ticketCount--;
                updateDisplay();
            }
        });

        updateDisplay(); 
    }
});


 document.addEventListener("DOMContentLoaded", function () {
    const timeInput = document.getElementById("time");
    if (timeInput) {
      flatpickr(timeInput, {
        enableTime: true,
        noCalendar: true,
        dateFormat: "h:i K",  
        time_24hr: false
      });
    }
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
