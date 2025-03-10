from app.infrastructure.database.db import db, AccountModel
from app.domain.account import Account

class AccountRepository:
    def __init__(self):
        self.db = db

    def add_account(self, account: Account):
        account_model = AccountModel(
            number=account.number,
            placeholder=account.placeholder,
            cvc_encrypted=account.cvc_encrypted,
            due_date=account.due_date,
            user_id=account.user_id,
            balance=account.balance
        )
        self.db.session.add(account_model)
        self.db.session.commit()
        self.db.session.refresh(account_model)
        return Account(
            id=account_model.id,
            number=account_model.number,
            placeholder=account_model.placeholder,
            cvc_encrypted=account_model.cvc_encrypted,
            due_date=account_model.due_date,
            user_id=account_model.user_id,
            balance=account_model.balance
        )

    def get_account_by_id(self, account_id: int):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        if account_model:
            return Account(
                id=account_model.id,
                number=account_model.number,
                placeholder=account_model.placeholder,
                cvc_encrypted=account_model.cvc_encrypted,
                due_date=account_model.due_date,
                user_id=account_model.user_id,
                balance=account_model.balance
            )
        return None

    def update_balance(self, account_id: int, amount: float):
        account_model = self.db.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        if account_model:
            account_model.balance += amount
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