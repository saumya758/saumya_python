class Account:
    def __init__(self, balance, pin):
        self.__balance = balance   # private
        self.__pin = pin

    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        return "Invalid PIN"

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt, pin):
        if pin == self.__pin and amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Invalid transaction")
