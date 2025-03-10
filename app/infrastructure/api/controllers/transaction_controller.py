from flask import request, jsonify
from app.application.transaction_service import TransactionService
from app.infrastructure.database.transaction_repository import TransactionRepository
from app.infrastructure.database.account_repository import AccountRepository

transaction_service = TransactionService(TransactionRepository(), AccountRepository())

def transfer():
    data = request.get_json()
    try:
        transaction = transaction_service.transfer(data['from_account_id'], data['to_account_id'], data['amount'])
        return jsonify({
            'id': transaction.id,
            'from_account_id': transaction.from_account_id,
            'to_account_id': transaction.to_account_id,
            'amount': transaction.amount
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
def get_transactions_by_account(account_id):
    transactions = transaction_service.get_transactions_by_account(account_id)
    return jsonify([{
        'id': transaction.id,
        'from_account_id': transaction.from_account_id,
        'to_account_id': transaction.to_account_id,
        'amount': transaction.amount
    } for transaction in transactions]), 200
