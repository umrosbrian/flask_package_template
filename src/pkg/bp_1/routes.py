from pkg.bp_1 import bp
from flask import render_template
from logging import getLogger

logger = getLogger(__name__)


@bp.route('/')
def index():
   return render_template('bp_1/index.html')
