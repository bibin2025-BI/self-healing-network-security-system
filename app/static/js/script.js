document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard Loaded');
    
    // Example: Fetch system status
    fetch('/api/system_status')
        .then(response => response.json())
        .then(data => {
            console.log('System Status:', data);
        })
        .catch(error => console.error('Error:', error));
});
