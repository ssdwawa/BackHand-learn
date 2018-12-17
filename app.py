from api import app
from models import db

# db.init_app(app)
if __name__ == "__main__":
    app.run(debug = True)
