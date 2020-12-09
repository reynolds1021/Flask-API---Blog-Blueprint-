from app import create_app, db
from app.models import User, Blog

app = create_app()


@app.shell_context_processor
def make_context():
    return{'db': db, 'User': User, 'Blog': Blog}



