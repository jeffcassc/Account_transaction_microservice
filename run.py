from flask import Flask
from app.infrastructure.api.routes import account_blueprint, transaction_blueprint
from app.infrastructure.database.db import db
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Crear las tablas en la base de datos (solo la primera vez)
with app.app_context():
    db.create_all()

app.register_blueprint(account_blueprint)
app.register_blueprint(transaction_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5001)