from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/hello')
def hello_world():
    return 'Hello, World!'