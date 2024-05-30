from flask import Flask
app = Flask(__name__)

# ----------------------------------------------------------------------------------------------------------------------
# register blueprints
# ----------------------------------------------------------------------------------------------------------------------
from pkg.main import bp as main_bp
app.register_blueprint(main_bp)
from pkg.bp_1 import bp as bp_1_bp
app.register_blueprint(bp_1_bp, url_prefix='/bp_1')

# ----------------------------------------------------------------------------------------------------------------------
# set up logging
# ----------------------------------------------------------------------------------------------------------------------
import os
if os.getenv('FLASK_DEBUG') == '1':
    from logging import getLogger
    from pyutils import com
    logger = getLogger(__name__)
    com.logging_to_console()


# ----------------------------------------------------------------------------------------------------------------------
# set the secret key
# The secret key is used to cryptographically-sign (not encrypt) the cookies used for storing the session data on the \
# client side.  This means that the user can see but can't change the cookie's values.
# ----------------------------------------------------------------------------------------------------------------------
import secrets
from flask_wtf import CSRFProtect
app.secret_key = secrets.token_urlsafe(16)
# Flask-WTF requires this line
csrf = CSRFProtect(app)
