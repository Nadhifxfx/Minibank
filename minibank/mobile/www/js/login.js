function login() {
    let username = document.getElementById('username').value;
    let pin = document.getElementById('pin').value;

    fetch("http://localhost/minibank/middleware/api/login.php", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, pin})
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "success") {
            document.getElementById("message").innerText = "Login berhasil! Selamat datang " + data.data.customer_name;
        } else {
            document.getElementById("message").innerText = data.message;
        }
    })
    .catch(err => console.log(err));
}
