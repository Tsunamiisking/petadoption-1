document.addEventListener('DOMContentLoaded', function() {
  let submitButton = document.querySelector("#submit-button");
  if (submitButton) {
    submitButton.disabled = true;
  }
  
  let confirmationInput = document.querySelector("#confirmation");
  if (confirmationInput) {
    confirmationInput.addEventListener('keyup', () => {
       let password = document.querySelector("#password").value;
       let pwdconfirm = document.querySelector("#confirmation").value;
       let passMismatch = document.querySelector(".pass-missmatch");
       if (pwdconfirm !== password) {
         submitButton.disabled = true;
         passMismatch.textContent = "Password Mismatch";
       } else {
         submitButton.disabled = false;
         passMismatch.textContent = "";
       }
    });
  }
});


document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll(".nav-item").forEach((item) => {
    item.addEventListener("click", () => {
      item.classList.add("active");
    });
  });
});
