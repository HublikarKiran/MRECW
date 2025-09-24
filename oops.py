from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.__balance = balance

    @abstractmethod
    def account_type(self):
        self._interst = self.__balance * 0.05
        self._service_fee = 10

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(
                f"Deposited {amount} into the account. Updated Balance ; {self.__balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        total_amount = amount + getattr(self, "_service_fee", 0)
        if total_amount <= self.__balance:
            self.__balance = self.__balance - total_amount
            print(
                f"Withdrew {total_amount} from the account. Updated Balance :{self.__balance}")
        else:
            print("Insufficient funds")


class SavingsAccount(BankAccount):
    def account_type(self):
        super().account_type()
        print(
            f"Savings Account: Interest Earned:{self._interest}, Service Fee:{self._service_fee}")


class CurrentAccount(BankAccount):
    def account_type(self):
        super().account_type()
        print(
            f"Current Account: Interest Earned:{self._interest}, Service Fee:{self._service_fee}")


class BankAccountWithOverload(SavingsAccount):
    def __add__(self, other):
        new_balance = self.get_balance() + other.get_balance()
        return BankAccountWithOverload(self.account_name, new_balance)


s1 = SavingsAccount("Rahul", 2000)
bal = s1.get_balance()
print(bal)
dep = s1.deposit(400)
print(dep)
wit = s1.withdraw(600)
print(wit)
