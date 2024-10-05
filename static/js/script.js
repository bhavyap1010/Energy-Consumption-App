// JavaScript to handle form submission and feedback display
document.getElementById('energyForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Simulate a successful submission (you can replace this with actual submission logic)
    setTimeout(function() {
        document.getElementById('feedback').style.display = 'block'; // Show success message
        document.getElementById('energyForm').reset(); // Reset the form
    }, 500); // Simulate a delay for user experience
});