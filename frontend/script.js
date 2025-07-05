const form = document.getElementById('reviewform');
const submitBtn = form.querySelector('button[type="submit"]');
const responseMsg = document.getElementById('responsemsg');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  submitBtn.disabled = true;
  submitBtn.innerText = "Submitting...";

  const data = {
    name: form.name.value,
    email: form.email.value,
    review: form.review.value,
  };

  try {
    const response = await fetch("http://localhost:8000/submit-review", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    // Show success message
    responseMsg.innerText = result.message || "Review submitted successfully!";
    responseMsg.style.color = "green";

    form.reset();
  } catch (err) {
    responseMsg.innerText = "Something went wrong. Please try again.";
    responseMsg.style.color = "red";
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerText = "Submit Review";
  }
});