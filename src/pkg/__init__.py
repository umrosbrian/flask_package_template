from flask import Flask
app = Flask(__name__)

# ----------------------------------------------------------------------------------------------------------------------
# register blueprints
# ----------------------------------------------------------------------------------------------------------------------
from pkg.main import bp as main_bp
app.register_blueprint(main_bp)
from pkg.bp_1 import bp as bp_1_bp
app.register_blueprint(bp_1_bp, url_prefix='/bp_1')