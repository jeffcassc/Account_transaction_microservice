from flask import Blueprint
from app.infrastructure.api.controllers.account_controller import create_account, get_account, recharge_account, purchase, send, delete_account
from app.infrastructure.api.controllers.transaction_controller import get_transactions_by_account

# Blueprint para cuentas
account_blueprint = Blueprint('account', __name__)

# Rutas para cuentas
account_blueprint.route('/accounts', methods=['POST'])(create_account)
account_blueprint.route('/accounts/<int:account_id>', methods=['GET'])(get_account)
account_blueprint.route('/accounts/<int:account_id>/recharge', methods=['POST'])(recharge_account)
account_blueprint.route('/accounts/<int:account_id>/purchase', methods=['POST'])(purchase)
account_blueprint.route('/accounts/send', methods=['POST'])(send)
account_blueprint.route('/accounts/<int:account_id>', methods=['DELETE'])(delete_account)

# Blueprint para transacciones
transaction_blueprint = Blueprint('transaction', __name__)

# Rutas para transacciones
transaction_blueprint.route('/accounts/<int:account_id>/transactions', methods=['GET'])(get_transactions_by_account)