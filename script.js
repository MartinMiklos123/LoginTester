const validUsers = [
    {username :"xmiklos1", password: "password1234_"},
    {username: "xmiklos12421", password: "password1234_"}
];


function validateUsername(username, msg) {
    const regex = /^[a-zA-Z0-9]+$/;

        if (username.length < 4) {
        msg.textContent = "username length must be greater than 4 characters"
        return 1
    }

    if (username.includes(" ")) {
        msg.textContent = "username can't include any space"
        return 1
    }


    if (! regex.test(username)) {
        msg.textContent = "username can't use special characters"
        return 1
    }


    if (username.length > 12) {
        msg.textContent = "username length must be less than 12 characters"
        return 1
    }

}


function validatePassword(password, msg) {
    const regex = /^[a-zA-Z0-9]+$/;

    if (password.length < 8) {
        msg.textContent ="password must contain at least 8 characters"
        return 1
    }

    if (regex.test(password)) {
        msg.textContent ="password must contain at least 1 special character"
        return 1
    }

}


function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");
    errorMessage.textContent = "";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";

    res = validateUsername(username, errorMessage);

    if (res == 1) {
        return
    }

    res1 = validatePassword(password, errorMessage);

    if (res1 == 1) {
        return
    }

    const user = validUsers.find(user => user.username == username)
    
    if (! user) {
        errorMessage.textContent = "user doesn't exist"
       return
    }
    const validUser = validUsers.find(user => user.username == username && user.password == password);
    if (! validUser) {
        errorMessage.textContent = "password doesn't match"
        return
    }

    window.location.replace("redirect.html")






}

