var socket;

function connect() {
    socket = io();
    var ifr = document.getElementById('container-frame');
    socket.on("state_change", function(){
        console.log("ok");
        ifr.src = ifr.src;
    });
    socket.on("restart", function(){
        window.location.href="/";
    });
}


