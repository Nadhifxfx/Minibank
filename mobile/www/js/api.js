const API_BASE = "https://your-middleware-domain/api";

async function callAPI(endpoint, method = "GET", data = null) {
    let options = {
        method: method,
        headers: {
            "Content-Type": "application/json",
        }
    };

    if (data) options.body = JSON.stringify(data);

    const response = await fetch(API_BASE + endpoint, options);
    return response.json();
}
