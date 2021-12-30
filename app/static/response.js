var timeleft = 20;
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
    parent.socket.emit("response", document.getElementById("response").value);
    document.getElementById("timer").innerHTML = "Auf andere Spieler warten ...";
    document.getElementById("response").readOnly = true;
    var commit = document.getElementById("commit")
    commit.enabled = false;
    commit.style.backgroundColor = "rgb(122, 190, 122)";
    commit.value = "Antwort bestätigt"
}

