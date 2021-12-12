from flask import Blueprint
from ..models import GamesHandler, PlayersHandler

games_handler = GamesHandler()
players_handler = PlayersHandler()

main = Blueprint('main', __name__, template_folder="templates")

from . import routes_settings, routes_game
