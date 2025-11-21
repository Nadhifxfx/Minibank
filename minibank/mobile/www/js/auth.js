function doLogin() {
  let username = document.getElementById("username").value;
  let pin = document.getElementById("pin").value;

  apiLogin(username, pin).then(result => {
    if (result.access_token) {
      localStorage.setItem("token", result.access_token);
      window.location.href = "dashboard.html";
    } else {
      alert("Login gagal!");
    }
  });
}
