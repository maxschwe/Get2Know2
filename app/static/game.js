var socket;
var ifr = document.getElementById('container-frame');

function connect() {
    socket = io();
}

socket.on("state_change", function(){
    console.log("ok");
    ifr.scr = ifr.src;
});
