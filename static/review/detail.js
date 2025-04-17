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

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {
  const likeButtons = document.querySelectorAll(".like-button");

  likeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const reviewId = button.dataset.reviewId;
      const toggleUrl = button.dataset.url;
      const csrftoken = getCookie("csrftoken");

      fetch(toggleUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": csrftoken,
        },
        body: `review_id=${reviewId}`,
      })
        .then((resp) => {
          if (!resp.ok) throw new Error("サーバーエラー");
          return resp.json();
        })
        .then((data) => {
          button.classList.toggle("liked", data.liked);
        })
        .catch((err) => console.error(err));
    });
  });
});
