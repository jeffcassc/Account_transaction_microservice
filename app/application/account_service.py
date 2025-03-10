import requests
from app.domain.account import Account
from app.infrastructure.database.account_repository import AccountRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, user_id, account_number, initial_balance=0):
        # Verificar si el usuario existe
        user_service_url = f"http://localhost:5000/users/{user_id}"  # URL del microservicio de usuarios
        response = requests.get(user_service_url)
        
        if response.status_code != 200:
            raise ValueError("User does not exist")

        # Crear la cuenta
        account = Account(id=None, user_id=user_id, account_number=account_number, balance=initial_balance)
        return self.account_repository.add_account(account)

    def get_account(self, account_id):
        return self.account_repository.get_account_by_id(account_id)

    def get_accounts_by_user(self, user_id):
        return self.account_repository.get_accounts_by_user_id(user_id)

    def update_balance(self, account_id, amount):
        return self.account_repository.update_balance(account_id, amount)
    
    def get_accounts_by_user(self, user_id):
        return self.account_repository.get_accounts_by_user_id(user_id)
    
    def update_account(self, account_id, account_number=None, balance=None):
        account = self.account_repository.get_account_by_id(account_id)
        if account:
            if account_number:
                account.account_number = account_number
            if balance is not None:
                account.balance = balance
            self.account_repository.update_account(account)
            return account
        return None
    
    def delete_account(self, account_id):
        return self.account_repository.delete_account(account_id)