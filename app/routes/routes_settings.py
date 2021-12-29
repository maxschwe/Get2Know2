from . import main, players_handler, games_handler
from flask import render_template, redirect, url_for, request, session


@main.route("/", methods=["GET", "POST"])
def index():
    if 'name' in session:
        name = session['name']
        game_id = session['game_id']
        error = session['error']
    else:
        name = game_id = error = ""
    return render_template("index.html", name=name, game_id=game_id, error=error)


@main.route("/join", methods=["POST", "GET"])
def join():
    if request.method == "GET":
        return redirect("/")
    if 'user_id' in session:
        try:
            games_handler.disconnect_game(
                session['game_id'], session['user_id'])
        except:
            pass
    name = request.form["name"]

    new_player = players_handler.new_player(name)
    session["name"] = name
    if request.form["join-btn"] == "join":
        game_id = request.form["game-id"]
        valid, error = games_handler.join_game(game_id, new_player)
        session['error'] = error
        if not valid:
            return redirect("/")
    else:
        game_id = games_handler.create_game(new_player)
    session["game_id"] = game_id
    session["user_id"] = new_player.id
    session["error"] = ""
    return redirect(f"/game/{game_id}")
