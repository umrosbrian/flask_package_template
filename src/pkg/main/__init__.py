from flask import Blueprint

bp = Blueprint('main', __name__)

from pkg.main import routes