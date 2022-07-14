from flask import Blueprint
# In the imports section, add this
from flask_login import login_required, current_user
from flask import render_template

bp = Blueprint("orders", __name__, url_prefix="")


# Make your index function look like this
@bp.route("/")
@login_required
def index():
    return render_template("orders.html")