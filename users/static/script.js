document.addEventListener('DOMContentLoaded', function() {
    const messageBox = document.getElementById('message-box');

    if (messageBox) {
        setTimeout(function() {
            messageBox.style.display = 'none';  // Completely hide after fade-out
        }, 3000);  // Fully hidden after 3 seconds
    }
});