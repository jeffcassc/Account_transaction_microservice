from app.domain.transaction import Transaction
from app.infrastructure.database.transaction_repository import TransactionRepository
from app.infrastructure.database.account_repository import AccountRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository, account_repository: AccountRepository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def add_transaction(self, account_id, type, amount):
        transaction = Transaction(
            id=None,
            account_id=account_id,
            type=type,
            amount=amount,
            date=None
        )
        return self.transaction_repository.add_transaction(transaction)

    def get_transactions_by_account(self, account_id):
        return self.transaction_repository.get_transactions_by_account_id(account_id)