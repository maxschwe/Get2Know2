var timeleft = 20;
var selected = -1;
var enabled = true;
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
  if (selected != 0){
    clearInterval(downloadTimer);
    parent.socket.emit("selection", selected);
    document.getElementById("timer").innerHTML = "Auf andere Spieler warten ...";
    var commit = document.getElementById("commit")
    commit.enabled = false;
    commit.style.backgroundColor = "rgb(122, 190, 122)";
    commit.value = "Antwort bestätigt"
  }
    
}

function selection(j, x){
  if (enabled) {
    var options = document.getElementsByClassName("selection");
    for (var i = 0; i < options.length; i++) {
      options[i].classList.remove("selected");
   }
   console.log(x);
    options[x-1].classList.add("selected");
      selected=j;
      console.log("selected: " + selected);
  }
  
}