from flask import Flask

from models import db
from routes import *
app = Flask(__name__)
app.register_blueprint(routes)
app.config.from_object('config.Config')

db.init_app(app)
with app.app_context():
    db.create_all()




if __name__ == '__main__':
    app.run()
