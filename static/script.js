// Add typing effect on homepage's heading
if (document.getElementById("auto-type")) {
    let typed = new Typed(".auto-type", {
        strings: ["notes", "ideas", "thoughts"],
        typeSpeed: 130,
        backSpeed: 130,
        loop: true
    });
}

const loginForm = document.getElementById("login-form");

// Check if user on login page or not
if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
        // Get form inputs
        let username = document.getElementById("username");
        let password = document.getElementById("password");
        let submit = true;
        
        // Validate user input
        // Check if the user has typed a username.
        if (username.value === "") {
            error(username, "Must include username.")
            submit = false;
        } 
        // Check if the username inputted is exists.
        else if (!is_in(username.value, users)) {
            error(username, "Username is not exists.")
            submit = false;
        }
        else {
            succuss(username);
        }
    
        // Check if the user has typed a password.
        if (password.value === "") {
            error(password, "Must include password");
            submit = false;
        }
        else {
            succuss(password);
        }
        
        if (!submit) {
            e.preventDefault();
        }
    });
}

const signUpForm = document.getElementById("signup-form");

if (signUpForm) {
    signUpForm.addEventListener("submit", (e) => {
        let username = document.getElementById("username");
        let password = document.getElementById("password");
        let confirmation = document.getElementById("confirmation");
        submit = true;

        // Validate username
        let regex = /^[A-Za-z][A-Za-z0-9_]{7,29}$/;
        isValid = regex.test(username.value);
        if (username.value === "") {
            error(username, "Must include username.")
        }
        else if (!isValid) {
            regexLength = /^.{8,20}$/;
            if (!regexLength.test(username.value)) {
                error(username, "Length must be 8 to 20 characters.")
            } else {
                error(username, "Only alphanumeric characters allowed.");
            }
            submit = false;
        }
        else {
            succuss(username);
        }

        if (is_in(username.value, users)) {
            error(username, "Username already exists.")
            submit = false;
        }

        // Validate password
        if (password.value === "") {
            error(password, "Must include password.");
            submit = false;
        }
        else if (!/^.{8,30}$/.test(password.value)) {
            console.log("Executed!")
            error(password, "Length must be 8 to 30.");
            submit = false;
        }
        else {
            succuss(password);
        }
        
        // Validate confirmation password
        if (confirmation.value === "") {
            error(confirmation, "Must include confirmation password.");
            submit = false;
        }
        else if (confirmation.value !== password.value) {
            error(confirmation, "Passwords don't match.");
            submit = false;
        }
        else {
            succuss(confirmation);
        }
        
        if (!submit) {
            e.preventDefault();
        }
    })
}

function error(field, message) {
    field.parentElement.className = "field error";
    field.parentElement.querySelector("small").innerHTML = message;
    // Convert check circle to exclamation point
    field.parentElement.querySelector("i").className = "bx bxs-error-circle";
}

function succuss(field) {
    field.parentElement.className = "field succuss";
    // Convert exclamation point to check circle
    field.parentElement.querySelector("i").className = "bx bxs-check-circle";
}

function is_in(username, users) {
    for (let i = 0; i < users.length; i++)
    {
        if (users[i][1] === username)
        {
            return true;
        }
    }
    return false;
}