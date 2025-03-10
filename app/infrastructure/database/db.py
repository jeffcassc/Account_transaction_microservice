from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccountModel(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)  # Relación con el microservicio de usuarios
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

class TransactionModel(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    from_account_id = db.Column(db.Integer, nullable=False)
    to_account_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

