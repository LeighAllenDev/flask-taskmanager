import os
from taskmanager import app, db
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=os.environ.get("DEBUG"),
    )
