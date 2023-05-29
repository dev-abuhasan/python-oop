class Phone:
    price = 1000
    color = 'blue'
    brand = 'car'

    def call(self):
        a = 'Abu Hasan Calling'
        b = "Double Qts"
        return a, b

    def math(self, x, y, z):
        sum = x + y + z
        sub = x - y + z
        mul = x * y * z
        dev = x * y / z
        return sum, sub, mul, dev


print(Phone())
print(Phone().brand)
print(Phone().color)
print(Phone().price)
print(Phone().call())
print(Phone().math(5, 4, 2))
