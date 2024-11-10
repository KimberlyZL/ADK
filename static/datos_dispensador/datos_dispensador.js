const options = {
    protocol: 'wss',
    port: 8084,
    clientId: 'web_client_' + Math.random().toString(16).substring(2, 8),
    username: 'kimberly',
    password: 'kimberly',
};

const brokerUrl = 'wss://z2729822.ala.us-east-1.emqxsl.com:8084/mqtt';

const client = mqtt.connect(brokerUrl, options);

client.on('connect', () => {
    console.log('Conectado al broker MQTT');
    client.subscribe('emqx/esp32', (err) => {
        if (!err) {
            console.log('Suscrito al tema');
        }
    });
});

client.on('message', (topic, message) => {
    console.log(`Mensaje recibido en el tema ${topic}: ${message.toString()}`);

    const data = JSON.parse(message.toString());

    const tbody = document.getElementById('dispensadores-tbody');

    const newRow = tbody.insertRow();

    const cell1 = newRow.insertCell(0);
    const cell2 = newRow.insertCell(1);
    const cell3 = newRow.insertCell(2);
    const cell4 = newRow.insertCell(3);


    const currentDate = new Date().toLocaleString();

    cell1.textContent = data.UID || 'N/A';
    cell2.textContent = data.distancia || 'N/A';
    cell3.textContent = data.estado || 'N/A';
    cell4.textContent = currentDate;

    sendDataToServer({
        distancia: data.distancia,
        estado: data.estado,
        UID: data.UID,
        fecha: currentDate
    });

    tbody.scrollTop = tbody.scrollHeight;
});

client.on('error', (err) => {
    console.error('Error de conexión:', err);
});

function sendDataToServer(data) {
    fetch('/guardar_datos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Datos enviados al servidor:', data);
    })
    .catch((error) => {
        console.error('Error al enviar los datos al servidor:', error);
    });
}
