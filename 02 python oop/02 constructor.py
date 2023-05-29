class Phone:
    manufactured = "Bangladesh"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phn, sms):
        text = f'Sending to: {phn} {sms}'
        return text


print(Phone('Abu', 'Samsung', 1234).send_sms('01778', 'Test Sms'))

a_p = Phone('Hasan', 'Samsung', 1234)
print(a_p.owner, a_p.price, a_p.brand)

a_p = Phone('Ah', 'Samsung', 1234)
print(a_p.owner, a_p.price, a_p.brand)