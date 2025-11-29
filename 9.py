from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid via UPI:", amount)

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid using Credit Card:", amount)

class Wallet(Payment):
    def pay(self, amount):
        print("Paid via Wallet:", amount)

p = [UPI(), CreditCard(), Wallet()]
for pay in p:
    pay.pay(500)
