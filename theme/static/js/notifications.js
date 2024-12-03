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

document.addEventListener("DOMContentLoaded", function () {
  const notificationList = document.getElementById("notification-list");

  function fetchNotifications() {
    fetch("/notifications/", {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        const notifications = data.notifications;
        notificationList.innerHTML = "";

        notifications.forEach((notification) => {
          const listItem = document.createElement("li");
          listItem.classList.add("text-xxs", "flex", "items-center", "space-x-3", "mx-3");

          // Create an image element for the notification (profile or icon)
          const img = document.createElement("img");
          img.src = notification.imageUrl;
          img.alt = "Notification Image"; 
          img.classList.add("w-10", "h-10", "rounded-full", "mx-30" , "my-3");

          // Create a clickable link for the notification message
          const link = document.createElement("a");
          link.href = notification.url;
          link.innerHTML = notification.message;
          link.classList.add("text-black", "flex-1", "text-xxs");

          // Append image and link to the list item
          listItem.appendChild(img);
          listItem.appendChild(link);

          // Append the list item to the notification list
          notificationList.appendChild(listItem);

          const hr = document.createElement("hr");
            hr.classList.add("border-t", "border-gray-300", "my-2");
            notificationList.appendChild(hr);
        });
      })
      .catch((error) =>
        console.error("Error fetching notifications:", error)
      );
  }

  // Poll every 10 seconds
  setInterval(fetchNotifications, 10000);
  fetchNotifications();
});




