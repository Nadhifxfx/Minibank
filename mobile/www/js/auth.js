async function login(username, pin) {
    const result = await callAPI("/auth/login", "POST", {
        username: username,
        pin: pin
    });

    if (result.status === "OK") {
        localStorage.setItem("token", result.data.token);
        localStorage.setItem("customer_id", result.data.customer_id);
        window.location.href = "pages/dashboard.html";
    } else {
        alert(result.message);
    }
}
