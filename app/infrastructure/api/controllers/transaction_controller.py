from flask import request, jsonify
from app.application.transaction_service import TransactionService
from app.infrastructure.database.transaction_repository import TransactionRepository
from app.infrastructure.database.account_repository import AccountRepository

transaction_service = TransactionService(TransactionRepository(), AccountRepository())

def get_transactions_by_account(account_id):
    transactions = transaction_service.get_transactions_by_account(account_id)
    return jsonify([{
        'id': transaction.id,
        'account_id': transaction.account_id,
        'type': transaction.type,
        'amount': transaction.amount,
        'date': transaction.date
    } for transaction in transactions]), 200