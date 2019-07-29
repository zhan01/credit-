class Product:
    
    def __init__(self, name, interest):
        self.name = name
        self.interest = interest / 100


class  Credit:

    def __init__(self, customer, product, amount):
        self.customer = customer   # Credit for customer
        self.product = product     # Product credit
        self.amount = amount       # Initial budget     
        self.cost = amount         # Cost of credit
        self.counter = 0
    
    def tick(self):
        self.cost += self.cost * self.product.interest  # Calculating credit
        self.counter += 1

    def pay(self, amount):
        self.cost = self.cost - amount #Deduct amount from credit
        if self.cost == 0:
            self.customer.credits.remove(self)

    def __str__(self):
        return  str(self.__dict__[item]for item in self.__dict__)
            

class Customer:

    def __init__(self, name, credits):
        self.name = name
        self.credits = []

    def take_credit(self, product, amount):
        credit = Credit(self, product, amount)
        self.credits.append(credit)
        return credit

    def pay(self, credit, amount):
        credit.pay(amount)

    def __str__(self):
        return str(self.__dict__)



car = Product('Car', 10)
home = Product('Home', 5)
alice = Customer('Alice', [])
charlie = Customer('Charlie', [])
credit1 = alice.take_credit(car, 1000)
credit2 = charlie.take_credit(home, 1000)
credit3 = charlie.take_credit(car, 1000)

print(alice)
print(charlie)


assert alice.credits == [credit1]
assert charlie.credits == [credit2, credit3]

credit1.tick()
credit2.tick()
credit3.tick()

assert credit1.cost == 1100
assert credit2.cost == 1050
assert credit3.cost == 1100
assert credit1.counter == 1

credit2.tick()
credit3.tick()

assert credit2.cost == 1102.5
assert credit3.cost == 1210
assert credit2.counter == 2

credit3.tick()

assert credit3.cost == 1331
assert credit3.counter == 3

alice.pay(credit1, 600) 
assert credit1.cost == 500
alice.pay(credit1, 500)   
assert credit1.cost == 0
assert alice.credits == []

charlie.pay(credit2, 1102.5)
assert credit2.cost == 0
assert charlie.credits == [credit3]
charlie.pay(credit3, 331)
assert credit3.cost == 1000
charlie.pay(credit3, 1000)
charlie.credits == []

