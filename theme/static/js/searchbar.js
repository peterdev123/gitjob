// Reference to the search input and search icon
const searchInput = document.querySelector("#search_job");
const searchIcon = document.querySelector(".search_job img");

// Function to filter job postings
const filterJobPostingsBySearch = () => {
  const searchText = searchInput.value.toLowerCase();
  const jobPostings = document.querySelectorAll(".job-posting"); // Adjust the selector to match your structure

  jobPostings.forEach((job) => {
    const jobTitle = job.querySelector("h1").textContent.toLowerCase();
    const companyName = job.querySelector("h6").textContent.toLowerCase();

    if (jobTitle.includes(searchText) || companyName.includes(searchText)) {
      job.style.display = "flex";
    } else {
      job.style.display = "none";
    }
  });
};

// Prevent default behavior on Enter key and trigger the filter
searchInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    filterJobPostingsBySearch();
  }
});

// Add click event to search icon
searchIcon.addEventListener("click", () => {
  filterJobPostingsBySearch();
});
