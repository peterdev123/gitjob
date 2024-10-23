const notifSidebar = document.getElementById("notif-sidebar");
const notifToggle = document.getElementById("notif-toggle");
const close_sidebar = document.getElementById("close-toggle-notif-sidebar");
const backdrop = document.getElementById("backdrop");

// Toggle notification sidebar visibility
notifToggle.addEventListener("click", () => {
  notifSidebar.classList.toggle("translate-x-full");
  backdrop.classList.toggle("hidden");
});

// Close notification sidebar when clicking on the close button
close_sidebar.addEventListener("click", () => {
  notifSidebar.classList.add("translate-x-full");
  backdrop.classList.add("hidden");
});

// Close notification sidebar when clicking anywhere but the sidebar
document.addEventListener("click", (event) => {
  if (
    !notifSidebar.contains(event.target) &&
    !notifToggle.contains(event.target)
  ) {
    notifSidebar.classList.add("translate-x-full");
    backdrop.classList.add("hidden");
  }
});

// Prevent clicks inside the notification sidebar from closing it
notifSidebar.addEventListener("click", (event) => {
  event.stopPropagation();
});
