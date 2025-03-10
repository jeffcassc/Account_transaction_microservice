from app.domain.transaction import Transaction
from app.infrastructure.database.transaction_repository import TransactionRepository
from app.infrastructure.database.account_repository import AccountRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository, account_repository: AccountRepository):
        self.transaction_repository = transaction_repository
        self.account_repository = account_repository

    def transfer(self, from_account_id, to_account_id, amount):
        # Verificar que las cuentas existan
        from_account = self.account_repository.get_account_by_id(from_account_id)
        to_account = self.account_repository.get_account_by_id(to_account_id)
        
        if not from_account or not to_account:
            raise ValueError("One or both accounts do not exist")

        # Verificar saldo suficiente
        if from_account.balance < amount:
            raise ValueError("Insufficient balance")

        # Actualizar saldos
        self.account_repository.update_balance(from_account_id, -amount)
        self.account_repository.update_balance(to_account_id, amount)

        # Registrar la transacción
        transaction = Transaction(id=None, from_account_id=from_account_id, to_account_id=to_account_id, amount=amount)
        return self.transaction_repository.add_transaction(transaction)
    
    def get_transactions_by_account(self, account_id):
            return self.transaction_repository.get_transactions_by_account_id(account_id)
