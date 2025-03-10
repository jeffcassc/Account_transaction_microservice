from app.infrastructure.database.db import db, AccountModel
from app.domain.account import Account

class AccountRepository:
    def __init__(self):
        self.db = db

    def add_account(self, account: Account):
        account_model = AccountModel(user_id=account.user_id, account_number=account.account_number, balance=account.balance)
        self.db.session.add(account_model)
        self.db.session.commit()
        self.db.session.refresh(account_model)
        return Account(id=account_model.id, user_id=account_model.user_id, account_number=account_model.account_number, balance=account_model.balance)

    def get_account_by_id(self, account_id: int):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        if account_model:
            return Account(id=account_model.id, user_id=account_model.user_id, account_number=account_model.account_number, balance=account_model.balance)
        return None

    def get_accounts_by_user_id(self, user_id: int):
        accounts = self.db.session.query(AccountModel).filter(AccountModel.user_id == user_id).all()
        return [Account(id=account.id, user_id=account.user_id, account_number=account.account_number, balance=account.balance) for account in accounts]

    def update_balance(self, account_id: int, amount: float):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        if account_model:
            account_model.balance += amount
            self.db.session.commit()
            return True
        return False
    
    def update_account(self, account: Account):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account.id).first()
        if account_model:
            account_model.account_number = account.account_number
            account_model.balance = account.balance
            self.db.session.commit()
            return True
        return False
    
    def delete_account(self, account_id: int):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        if account_model:
            self.db.session.delete(account_model)
            self.db.session.commit()
            return True
        return False