import requests
from app.domain.account import Account
from app.infrastructure.database.account_repository import AccountRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, number, placeholder, cvc_encrypted, due_date, user_id, initial_balance=0):
        # Verificar si el usuario existe
        user_service_url = f"http://localhost:5000/users/{user_id}"  # URL del microservicio de usuarios
        response = requests.get(user_service_url)
        
        if response.status_code != 200:
            raise ValueError("User does not exist")

        # Crear la cuenta
        account = Account(
            id=None,
            number=number,
            placeholder=placeholder,
            cvc_encrypted=cvc_encrypted,
            due_date=due_date,
            user_id=user_id,
            balance=initial_balance
        )
        return self.account_repository.add_account(account)

    def get_account(self, account_id):
        return self.account_repository.get_account_by_id(account_id)

    def update_balance(self, account_id, amount):
        return self.account_repository.update_balance(account_id, amount)

    def delete_account(self, account_id):
        return self.account_repository.delete_account(account_id)

    def recharge(self, account_id, amount):
        return self.account_repository.update_balance(account_id, amount)

    def purchase(self, account_id, amount):
        account = self.account_repository.get_account_by_id(account_id)
        if account.balance < amount:
            raise ValueError("Insufficient balance")
        return self.account_repository.update_balance(account_id, -amount)

    def send(self, from_account_id, to_account_id, amount):
        from_account = self.account_repository.get_account_by_id(from_account_id)
        to_account = self.account_repository.get_account_by_id(to_account_id)
        
        if not from_account or not to_account:
            raise ValueError("One or both accounts do not exist")

        if from_account.balance < amount:
            raise ValueError("Insufficient balance")

        self.account_repository.update_balance(from_account_id, -amount)
        self.account_repository.update_balance(to_account_id, amount)