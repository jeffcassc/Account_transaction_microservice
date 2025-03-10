from flask import Blueprint
from app.infrastructure.api.controllers.account_controller import create_account, delete_account, get_account, get_accounts_by_user, update_account
from app.infrastructure.api.controllers.transaction_controller import transfer, get_transactions_by_account

# Blueprint para cuentas
account_blueprint = Blueprint('account', __name__)

# Rutas para cuentas
account_blueprint.route('/accounts', methods=['POST'])(create_account)
account_blueprint.route('/accounts/<int:account_id>', methods=['GET'])(get_account)
account_blueprint.route('/users/<int:user_id>/accounts', methods=['GET'])(get_accounts_by_user)
account_blueprint.route('/accounts/<int:account_id>', methods=['PUT'])(update_account)
account_blueprint.route('/accounts/<int:account_id>', methods=['DELETE'])(delete_account)

# Blueprint para transacciones
transaction_blueprint = Blueprint('transaction', __name__)

# Rutas para transacciones
transaction_blueprint.route('/transactions', methods=['POST'])(transfer)
transaction_blueprint.route('/accounts/<int:account_id>/transactions', methods=['GET'])(get_transactions_by_account)