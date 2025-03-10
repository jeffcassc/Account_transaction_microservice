from app.infrastructure.database.db import db, TransactionModel
from app.domain.transaction import Transaction

class TransactionRepository:
    def __init__(self):
        self.db = db

    def add_transaction(self, transaction: Transaction):
        # Asegúrate de que este bloque esté indentado
        transaction_model = TransactionModel(
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
            date=transaction.date
        )
        self.db.session.add(transaction_model)
        self.db.session.commit()
        self.db.session.refresh(transaction_model)
        return Transaction(
            id=transaction_model.id,
            account_id=transaction_model.account_id,
            type=transaction_model.type,
            amount=transaction_model.amount,
            date=transaction_model.date
        )

    def get_transactions_by_account_id(self, account_id: int):
        transactions = self.db.session.query(TransactionModel).filter(
            TransactionModel.account_id == account_id
        ).all()
        return [Transaction(
            id=transaction.id,
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
            date=transaction.date
        ) for transaction in transactions]