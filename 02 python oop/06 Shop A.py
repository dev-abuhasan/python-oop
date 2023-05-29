class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []  # cart is an instant att

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_cart(self, item):
        for product in self.cart:
            if product['item'] == item:
                self.cart.remove(product)
                break
        else:
            print(f"{item} is not in the cart.")

    def checkout(self, amt):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']

        if total > amt:
            return f'Cash={amt}, Cost={total}, Taka Kom Ache {total - amt}'
        else:
            return f'Cash={amt}, Cost={total}, Current Bal {amt - total}'


abu = Shop('ABU_SHOP')
abu.add_to_cart('Alu', 20, 5)
abu.add_to_cart('Dim', 35, 2)
abu.add_to_cart('Rice', 25, 5)

print(abu.cart)

print(abu.checkout(600))

print(abu.checkout(200))
abu.remove_cart('Dim')
print(abu.checkout(200))

abu.remove_cart('Rice')
print(abu.checkout(200))