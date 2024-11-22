console.log("JavaScript file loaded");
    
      const rangeInputs = document.querySelectorAll(".range-input input"),
        priceInputs = document.querySelectorAll(".price-input input"),
        range = document.querySelector(".slider .progress"),
        jobPostings = document.querySelectorAll(".job-posting"),
        jobFieldDropdown = document.getElementById("job-field");
        const scheduleInputs = document.querySelectorAll("input[name='full_time'], input[name='part_time'], input[name='internship'], input[name='project_work']");

// Add a click event listener to each schedule radio button
let lastCheckedRadio = null; // Keep track of the last checked radio button

scheduleInputs.forEach((input) => {
  input.addEventListener("click", function () {
    // If the same radio button is clicked again, uncheck it
    if (lastCheckedRadio === this) {
      this.checked = false;
      lastCheckedRadio = null; // Reset the last checked radio button
    } else {
      lastCheckedRadio = this; // Update the last checked radio button
    }
    // Trigger filtering after toggle
    filterJobPostings();
  });
});


// Function to get the selected schedule
const getSelectedSchedule = () => {
  const selected = [...scheduleInputs].find(input => input.checked);
  return selected ? selected.id : null; // Return the selected schedule ID or null if none is selected
};
    
      const priceGap = 1000; // Minimum gap between min and max values
    
      // Helper function to update the range slider's progress bar
      const updateSlider = (minVal, maxVal) => {
        range.style.left = ((minVal / rangeInputs[0].max) * 100).toFixed(2) + "%";
        range.style.right = (100 - (maxVal / rangeInputs[1].max) * 100).toFixed(2) + "%";
      };
    
      // Function to filter job postings based on the selected salary range and job field
      const filterJobPostings = () => {
    console.log("filterJobPostings called");
    const minSalary = parseInt(priceInputs[0].value, 10) || 0;
    const maxSalary = parseInt(priceInputs[1].value, 10) || 100000;
    const selectedJobField = jobFieldDropdown.value;
    const selectedSchedule = getSelectedSchedule(); // Get selected schedule

    console.log(`Filtering with minSalary: ${minSalary}, maxSalary: ${maxSalary}, jobField: ${selectedJobField}, schedule: ${selectedSchedule}`); // Debugging line

    jobPostings.forEach((job) => {
      const jobMinSalary = parseInt(job.getAttribute("data-min-salary"), 10);
      const jobMaxSalary = parseInt(job.getAttribute("data-max-salary"), 10);
      const jobField = job.getAttribute("data-job-field");
      const jobSchedule = job.getAttribute("data-job-sched"); // Assume a data attribute for job schedule

      // Check salary, job field, and schedule conditions
      const isSalaryMatch =
        !isNaN(jobMinSalary) &&
        !isNaN(jobMaxSalary) &&
        jobMaxSalary >= minSalary &&
        jobMinSalary <= maxSalary;

      const isJobFieldMatch =
        !selectedJobField || selectedJobField === jobField || selectedJobField === "any";

      const isScheduleMatch =
        !selectedSchedule || selectedSchedule === jobSchedule;

      if (isSalaryMatch && isJobFieldMatch && isScheduleMatch) {
        job.style.display = "block";
      } else {
        job.style.display = "none";
      }
    });
  };
    
      // Initialize the slider positions on page load
      window.addEventListener("load", () => {
        const minPrice = 0; // Initial min price
        const maxPrice = 100000; // Initial max price
    
        // Set initial values for both price and range inputs
        priceInputs[0].value = minPrice;
        priceInputs[1].value = maxPrice;
        rangeInputs[0].value = minPrice;
        rangeInputs[1].value = maxPrice;
    
        updateSlider(minPrice, maxPrice);
        filterJobPostings(); // Initial filter on page load
      });
    
      // Update slider and price inputs when price input fields are changed
      priceInputs.forEach((input) => {
        input.addEventListener("input", (e) => {
          console.log("Price input changed:", e.target.value); // Debugging line
          const minPrice = parseInt(priceInputs[0].value, 10);
          const maxPrice = parseInt(priceInputs[1].value, 10);
    
          if (maxPrice - minPrice >= priceGap) {
            if (e.target.classList.contains("input-min")) {
              rangeInputs[0].value = minPrice;
            } else {
              rangeInputs[1].value = maxPrice;
            }
            updateSlider(minPrice, maxPrice);
            filterJobPostings(); // Ensure this line is here
          }
        });
      });
    
      // Handle range sliders when moved
      rangeInputs.forEach((input) => {
        input.addEventListener("input", (e) => {
          console.log("Range input changed:", e.target.value); // Debugging line
          const minVal = parseInt(rangeInputs[0].value, 10);
          const maxVal = parseInt(rangeInputs[1].value, 10);
    
          if (maxVal - minVal < priceGap) {
            if (e.target.classList.contains("range-min")) {
              rangeInputs[0].value = maxVal - priceGap;
            } else {
              rangeInputs[1].value = minVal + priceGap;
            }
          } else {
            priceInputs[0].value = minVal;
            priceInputs[1].value = maxVal;
            updateSlider(minVal, maxVal);
            filterJobPostings(); // Ensure this line is here
          }
        });
      });
    
      // Add event listener to the Job Field dropdown
      jobFieldDropdown.addEventListener("change", () => {
        console.log("Job Field dropdown changed:", jobFieldDropdown.value); // Debugging line
        filterJobPostings();
      });
      window.addEventListener("load", () => {
    filterJobPostings();
  });