const rangeInputs = document.querySelectorAll(".range-input input"),
  priceInputs = document.querySelectorAll(".price-input input"),
  range = document.querySelector(".slider .progress");

let priceGap = 10000; // Minimum gap between min and max values

// Helper function to update the range slider's progress bar
const updateSlider = (minVal, maxVal) => {
  range.style.left = ((minVal / rangeInputs[0].max) * 100).toFixed(2) + "%";
  range.style.right =
    (100 - (maxVal / rangeInputs[1].max) * 100).toFixed(2) + "%";
};

// Initialize the slider positions on page load
window.addEventListener("load", () => {
  let minPrice = parseInt(priceInputs[0].value),
    maxPrice = parseInt(priceInputs[1].value);

  rangeInputs[0].value = minPrice;
  rangeInputs[1].value = maxPrice;
  updateSlider(minPrice, maxPrice);
});

// Update slider and price inputs when the price input fields are changed
priceInputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minPrice = parseInt(priceInputs[0].value),
      maxPrice = parseInt(priceInputs[1].value);

    // Ensure the gap between min and max is respected
    if (maxPrice - minPrice >= priceGap) {
      if (e.target.classList.contains("input-min")) {
        rangeInputs[0].value = minPrice;
      } else {
        rangeInputs[1].value = maxPrice;
      }
      updateSlider(minPrice, maxPrice);
    }
  });
});

// Handle the range sliders when they are moved
rangeInputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minVal = parseInt(rangeInputs[0].value),
      maxVal = parseInt(rangeInputs[1].value);

    // Prevent sliders from crossing over
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
    }
  });
});
