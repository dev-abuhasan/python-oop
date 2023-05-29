class Bank:

    def __init__(self, bal):
        self.bal = bal
        self.min_with = 100
        self.max_with = 100000

    def get_balance(self):
        return self.bal

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount

    def withdraw(self, amount):
        if amount < self.min_with:
            return f'Fokinni, You can withdraw below {self.min_with}'
        elif amount > self.get_balance():
            return f'Tor taka ache {self.get_balance()} ar uthabi {amount} tor ki mone hoi bank dibo tore huh! {amount - self.get_balance()} taka'
        elif amount > self.max_with:
            return f'bank fokir hbe. You can not with more than {self.max_with}'
        else:
            self.bal -= amount
            return f'Here is you current money {self.get_balance()} after withdraw'


dbbl = Bank(600500)
print(dbbl.withdraw(700300))
print(dbbl.withdraw(25))
print(dbbl.withdraw(500000))
print(dbbl.withdraw(1000))
print(dbbl.withdraw(200))
print(dbbl.withdraw(700300))
