class Account:
    def __init__(self, id, number, placeholder, cvc_encrypted, due_date, user_id, balance):
        self.id = id
        self.number = number
        self.placeholder = placeholder
        self.cvc_encrypted = cvc_encrypted
        self.due_date = due_date
        self.user_id = user_id
        self.balance = balance