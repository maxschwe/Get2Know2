from flask import Blueprint

main = Blueprint('main', __name__, template_folder="templates")

from . import routes_settings, routes_game
from . import routes_settings
