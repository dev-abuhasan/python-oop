# Abu Poribohon

class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []


class Driver:
    def __init__(self, name, license, age) -> None:
        self.name = name
        self.license = license
        self.age = age


class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self, start, desg):
        pass

class Passenger:
    pass

class Supervisor:
    pass


zakir_mia = Driver('Zakir Hossain', '123', 38)