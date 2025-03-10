class Transaction:
    def __init__(self, id, from_account_id, to_account_id, amount):
        self.id = id
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
        self.amount = amount