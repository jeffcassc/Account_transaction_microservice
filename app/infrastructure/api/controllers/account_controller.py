from flask import request, jsonify
from app.application.account_service import AccountService
from app.infrastructure.database.account_repository import AccountRepository

account_service = AccountService(AccountRepository())

def create_account():
    data = request.get_json()
    account = account_service.create_account(
        number=data['number'],
        placeholder=data['placeholder'],
        cvc_encrypted=data['cvc_encrypted'],
        due_date=data['due_date'],
        user_id=data['user_id'],
        initial_balance=data.get('initial_balance', 0)
    )
    return jsonify({
        'id': account.id,
        'number': account.number,
        'placeholder': account.placeholder,
        'cvc_encrypted': account.cvc_encrypted,
        'due_date': account.due_date,
        'user_id': account.user_id,
        'balance': account.balance
    }), 201

def get_account(account_id):
    account = account_service.get_account(account_id)
    if account:
        return jsonify({
            'id': account.id,
            'number': account.number,
            'placeholder': account.placeholder,
            'cvc_encrypted': account.cvc_encrypted,
            'due_date': account.due_date,
            'user_id': account.user_id,
            'balance': account.balance
        }), 200
    return jsonify({'error': 'Account not found'}), 404

def recharge_account(account_id):
    data = request.get_json()
    try:
        account_service.recharge(account_id, data['amount'])
        return jsonify({'message': 'Recharge successful'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def purchase(account_id):
    data = request.get_json()
    try:
        account_service.purchase(account_id, data['amount'])
        return jsonify({'message': 'Purchase successful'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def send():
    data = request.get_json()
    try:
        account_service.send(data['from_account_id'], data['to_account_id'], data['amount'])
        return jsonify({'message': 'Transfer successful'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def delete_account(account_id):
    if account_service.delete_account(account_id):
        return jsonify({'message': 'Account deleted successfully'}), 200
    return jsonify({'error': 'Account not found'}), 404