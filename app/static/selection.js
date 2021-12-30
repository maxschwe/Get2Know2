var timeleft = 20;
var selected = 0;
var downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
    submit_clicked();
  } else {
    document.getElementById("timer").innerHTML = timeleft + " Sekunden verbleibend";
  }
  timeleft -= 1;
}, 1000);

function submit_clicked(){
    clearInterval(downloadTimer);
    parent.socket.emit("selection", selected);
    document.getElementById("timer").innerHTML = "Auf andere Spieler warten ...";
    document.getElementById("fldak;sj").enabled = false;
}

function selection(i){
    selected=i;
    console.log("selected: " + selected);
}