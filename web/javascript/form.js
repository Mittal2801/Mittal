document.getElementById("loginform").addEventListener("submit",function(event){     
            
    event.preventDefault();
    
    let username = document.getElementById("username").value.trim();
    let usernameError = document.getElementById("usernameError");
    if (username.trim() === "") {
        usernameError.textContent = "Username is required";
        isValid = false;
    } 
    else {
        usernameError.textContent = "";
    }

    let email = document.getElementById("email").value.trim();
    let emailError = document.getElementById("emailError");
    if (email.trim() === "") {
        emailError.textContent = "Email is required";
        isValid = false;
    }
    else {
        emailError.textContent = "";
    }

    let password = document.getElementById("password").value.trim();
    let passwordError = document.getElementById("passwordError");

    if(password.length < 6) {
        passwordError.textContent = "Password must be 6 later";
        isValid = false;
    }
    else {
        passwordError.textContent = "";
    }

    let phone = document.getElementById("phone").value.trim();
    let phoneError = document.getElementById("phoneError");

    if (phone.length < 10) {
        phoneError.textContent = "Mobile number must be 10 numbers";
        isValid = false;
    }
    else {
        phoneError.textContent = "";
    }

    let age = document.getElementById("age").value.trim();
    let ageError = document.getElementById("ageError");

    if (age < 18 && age > 40 ) {
        ageError.textContent = "Not valid age";
        isValid = false;
    }
    else {
        ageError.textContent = "";
    }


    if (isValid) {
        alert("Form submitted successfully!!");
    }

});

let UpperCase = false;
let LowerCase = false;
let Number = false;
let SpecialChar = false;
let Length = false;

for (let i = 0; i < password.length; i++) {
    let char = password[i];

    if(password.length <= 8) {
        Length = true;
    }

    if (char >= 'A' && char <= 'Z') {
        hasUpperCase = true;
        
    }

    if (char >= 'a' && char <= 'z') {
        hasLowerCase = true;
    }

    if (char >= '0' && char <= '9') {
        hasNumber = true;
    }

    if (!(char >= 'A' && char <= 'Z') && !(char >= 'a' && char <= 'z') && !(char >= '0' && char <= '9')) {
        hasSpecialChar = true;
    }
}
if (UpperCase && LowerCase && Number && SpecialChar && Length) {
    passwordError.textContent = "";
} 
else if (UpperCase || LowerCase || !Number || !SpecialChar || !Length) {
    passwordError.textContent ="Password must contain at least one uppercase letter.";
    passwordError.textContent ="Password must contain at least one lowercase letter.";
    passwordError.textContent ="Password must contain at least number.";
    passwordError.textContent ="Password must contain at least one special character.";
    passwordError.textContent ="Password must contain at least eight character.";
}
else {
    passwordError.textContent ="Password must contain at least one uppercase letter, one lowercase letter, one number,one special character,and password must be 8 character.";
}