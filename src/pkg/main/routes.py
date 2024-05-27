# from pkg import app
from pkg.main import bp
from flask import render_template

@bp.route('/')
def index():
    user = {'username': 'Brian'}
    return render_template('index.html', title='Home', user=user)