async function fetchBalance() {
    let cust_id = localStorage.getItem("customer_id");

    const result = await callAPI(`/account/balance/${cust_id}`, "GET");

    if (result.status === "OK") {
        document.getElementById("saldo").innerText =
            result.data.available_balance;
    } else {
        alert(result.message);
    }
}
