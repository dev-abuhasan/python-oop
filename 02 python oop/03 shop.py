class Shop:
    cart = [] # class att 

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


abu = Shop('ABU_SHOP')
abu.add_to_cart('Bata Sandle')
abu.add_to_cart('T Shart')
print(abu.cart)

miya = Shop('Miya_SHOP')
miya.add_to_cart('Bata Sandle')
miya.add_to_cart('T Shart')
print(miya.cart)
