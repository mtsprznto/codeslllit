fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => {
        document.cookie = `client_ip=${data.ip}; path=/`;
    });