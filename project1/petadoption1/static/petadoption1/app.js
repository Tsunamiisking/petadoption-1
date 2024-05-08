document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#submit-button").disabled = true;
    document.querySelector("#confirmation").addEventListener('keyup', () => {
       let password = document.querySelector("#password").value;
       let pwdconfirm = document.querySelector("#confirmation").value;
       if (pwdconfirm !== password) {
         document.querySelector("#submit-button").disabled = true;
         document.querySelector(".pass-missmatch").textContent = "Password Mismatch";
       }else {
         document.querySelector("#submit-button").disabled = false;
         document.querySelector(".pass-missmatch").textContent = "";
       }
    });
 });