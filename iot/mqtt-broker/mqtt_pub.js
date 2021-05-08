var mqtt = require('mqtt');
var client  = mqtt.connect('mqtt://2.tcp.ngrok.io:14602');   //  write mqtt server ip here on esp8266 running
client.on('connect', function () {
setInterval(function() {
client.publish('TOPIC', 'ON');  // first parameter topic hai aur dosra hamara message hai
console.log('Message Sent');
}, 8000);    //  here 5000 is the 5 sec delay time

setInterval(function() {
    client.publish('TOPIC', 'OFF');  // first parameter topic hai aur dosra hamara message hai
    console.log('Message Sent');
    }, 9000);    //  here 5000 is the 5 sec delay time
    

});
