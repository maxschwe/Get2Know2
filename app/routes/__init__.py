from flask import Blueprint
from ..models import GamesHandler, PlayersHandler

players_handler = PlayersHandler()
games_handler = GamesHandler()

main = Blueprint('main', __name__)

if True:
    from . import routes_settings, routes_game, routes_lobby
