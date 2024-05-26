from flask import Blueprint

bp = Blueprint('bp_1', __name__)

from pkg.bp_1 import routes