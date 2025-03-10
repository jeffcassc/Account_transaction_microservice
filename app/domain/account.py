class Account:
    def __init__(self, id, user_id, account_number, balance):
        self.id = id
        self.user_id = user_id  # Relación con el microservicio de usuarios
        self.account_number = account_number
        self.balance = balance