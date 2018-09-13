from app_mod import app, db
from app_mod.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}

if __name__ == "__main__":
    app.run()