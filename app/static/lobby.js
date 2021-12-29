var slideIndex;

parent.socket.on("update_user_list", function(player_names){
    var player_list = document.getElementById("ul-player-list");
    player_list.innerHTML = '';
    player_names.forEach((player_name) => {
        var li = document.createElement('li');
        li.innerHTML = '<h3>' + player_name + '</h3>';
        li.classList.add("player-name");
        li.id = "player-name-item"
        player_list.appendChild(li);
    });
});
parent.socket.on("changed_category", function(category_num){
    showDivs(category_num);
});

parent.socket.on("changed_rounds", function(rounds){
    document.getElementById('num-game').value=rounds; 
    document.getElementById('sl-num-games').value = rounds;
});

function init_slideshow(index) {
    slideIndex = index;
    showDivs(slideIndex);
}

function plusDivs(n) {
    showDivs(slideIndex + n);
    parent.socket.emit("changed-category", slideIndex);
}

function showDivs(n) {
    var i;
    slideIndex = n;
    var x = document.getElementsByClassName("category");
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex-1].style.display = "block";
}

function updateTextInput(val) {
    document.getElementById('num-game').value=val;
    parent.socket.emit("changed-rounds", val)
};

function btn_start_game_clicked() {
    parent.socket.emit("start-game");
}