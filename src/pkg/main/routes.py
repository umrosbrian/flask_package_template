# from pkg import app
from pkg.main import bp
from flask import render_template
from logging import getLogger

logger = getLogger(__name__)

@bp.route('/')
def index():
    user = {'username': 'Brian'}
    return render_template('index.html', title='Home', user=user)