from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix='/blogs')

from app.blueprints.blog import routes