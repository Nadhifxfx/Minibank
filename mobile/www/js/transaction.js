async function doTransfer() {

    const cust_id = localStorage.getItem("customer_id");

    const data = {
        customer_id: cust_id,
        from: document.getElementById("from_acc").value,
        to: document.getElementById("to_acc").value,
        amount: parseFloat(document.getElementById("amount").value)
    };

    const result = await callAPI("/transaction/transfer", "POST", data);

    if (result.status === "OK") {
        alert("Transfer berhasil. Ref: " + result.data.reference);
    } else {
        alert(result.message);
    }
}
