var server_port = 65432;
var server_addr = "192.168.137.141";   // the IP address of your Raspberry PI

document.onkeydown = updateKey;
document.onload = send_data("page loaded");

function client(){
    
    const net = require('net');
    var input = document.getElementById("message").value;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}\r\n`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        document.getElementById("greet_from_server").innerHTML = data;
        console.log(data.toString());
        // client.end();
        // client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}

function send_data(msg){
    const net = require('net');
    // var input = document.getElementById("message").value;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${msg}\r\n`);
    });

    // get the data from the server
    client.on('data', (data) => {
        const obj = JSON.parse(data.toString());
        console.log(obj);
        insert(obj.timestamp, obj.name);
        // document.getElementById("cpu_temperature").innerHTML = obj.cpu_temperature;
        // document.getElementById("gpu_temperature").innerHTML = obj.gpu_temperature;
        // document.getElementById("battery").innerHTML = obj.battery;
        // document.getElementById("direction").innerHTML = obj.car_direction;

        // client.end();
        // client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}

function insert(timestamp, name) {
    var table = document.getElementById("timeTable");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = timestamp;
    cell2.innerHTML = name;
}

// function updateKey(e) {
//     e = e || window.event;

//     if (e.keyCode == '87') {
//         // up (w)
//         console.log("up");
//         document.getElementById("upArrow").style.color = "green";
//         insert("current time", "Kaylin")
//     }
//     else if (e.keyCode == '83') {
//         // down (s)
//         console.log("down");
//         document.getElementById("downArrow").style.color = "green";
//         send_data("backward");

//     }
//     else if (e.keyCode == '65') {
//         // left (a)
//         console.log("left");
//         document.getElementById("leftArrow").style.color = "green";
//         send_data("left");

//     }
//     else if (e.keyCode == '68') {
//         // right (d)
//         document.getElementById("rightArrow").style.color = "green";
//         send_data("right");
//     }
// }

