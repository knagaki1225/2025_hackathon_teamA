function openPopup() {
  document.getElementById("reviewPopup").style.display = "block";
}

function closePopup() {
  document.getElementById("reviewPopup").style.display = "none";
}

function setRating(val) {
  const rating = parseInt(val);
  document.getElementById("rating").value = rating;
  const stars = document.querySelectorAll(".star");
  stars.forEach((star, index) => {
    star.textContent = index < rating ? "★" : "☆";
    star.style.color = index < rating ? "red" : "black";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const stars = document.querySelectorAll(".star");
  stars.forEach((star) => {
    star.addEventListener("click", () => {
      const rating = star.getAttribute("data-value");
      setRating(rating);
    });
  });
});
