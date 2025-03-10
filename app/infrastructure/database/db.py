from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class AccountModel(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(20), unique=True, nullable=False)
    placeholder = db.Column(db.String(100), nullable=False)
    cvc_encrypted = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

class TransactionModel(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Enum('income', 'outcome'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)