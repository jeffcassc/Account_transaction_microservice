from app.infrastructure.database.db import db, TransactionModel
from app.domain.transaction import Transaction

class TransactionRepository:
    def __init__(self):
        self.db = db

    def add_transaction(self, transaction: Transaction):
        transaction_model = TransactionModel(from_account_id=transaction.from_account_id, to_account_id=transaction.to_account_id, amount=transaction.amount)
        self.db.session.add(transaction_model)
        self.db.session.commit()
        self.db.session.refresh(transaction_model)
        return Transaction(id=transaction_model.id, from_account_id=transaction_model.from_account_id, to_account_id=transaction_model.to_account_id, amount=transaction_model.amount)
    
    def get_transactions_by_account_id(self, account_id: int):
        transactions = self.db.session.query(TransactionModel).filter(
            (TransactionModel.from_account_id == account_id) | (TransactionModel.to_account_id == account_id)
        ).all()
        return [Transaction(id=transaction.id, from_account_id=transaction.from_account_id, to_account_id=transaction.to_account_id, amount=transaction.amount) for transaction in transactions]