from pkg.bp_1 import bp
from flask import render_template


@bp.route('/')
def index():
   return render_template('bp_1/index.html')
