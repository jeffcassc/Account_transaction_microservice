from flask import request, jsonify
from app.application.account_service import AccountService
from app.infrastructure.database.account_repository import AccountRepository

account_service = AccountService(AccountRepository())

def create_account():
    data = request.get_json()
    account = account_service.create_account(data['user_id'], data['account_number'], data.get('initial_balance', 0))
    return jsonify({
        'id': account.id,
        'user_id': account.user_id,
        'account_number': account.account_number,
        'balance': account.balance
    }), 201

def get_account(account_id):
    account = account_service.get_account(account_id)
    if account:
        return jsonify({
            'id': account.id,
            'user_id': account.user_id,
            'account_number': account.account_number,
            'balance': account.balance
        }), 200
    return jsonify({'error': 'Account not found'}), 404

def get_accounts_by_user(user_id):
    accounts = account_service.get_accounts_by_user(user_id)
    return jsonify([{
        'id': account.id,
        'user_id': account.user_id,
        'account_number': account.account_number,
        'balance': account.balance
    } for account in accounts]), 200

def update_account(account_id):
    data = request.get_json()
    account = account_service.update_account(account_id, data.get('account_number'), data.get('balance'))
    if account:
        return jsonify({
            'id': account.id,
            'user_id': account.user_id,
            'account_number': account.account_number,
            'balance': account.balance
        }), 200
    return jsonify({'error': 'Account not found'}), 404

def delete_account(account_id):
    if account_service.delete_account(account_id):
        return jsonify({'message': 'Account deleted successfully'}), 200
    return jsonify({'error': 'Account not found'}), 404


