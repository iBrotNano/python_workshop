class BankAccount:
    def __init__(self, iban, owner):
        self.iban = iban
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance += amount

    def transfer(self, amount, to):
        self.balance -= amount
        to.balance += amount


account1 = BankAccount("123-456", "Alice Adrian")
print(f"{account1=}")
print("memory address as hex", hex(id(account1)))

account2 = BankAccount("934-642", "Bob Builder")
print(f"{account2=}")
print("memory address as hex", hex(id(account2)))

print(f"{account1.balance=}")
print(f"{account1.iban=}")
print(f"{account1.owner=}")
print(f"{account2.balance=}")
print(f"{account2.iban=}")
print(f"{account2.owner=}")

account1.deposit(500)
print(f"{account1.balance=}")
account1.transfer(200, account2)

print(f"{account1.balance=}")
print(f"{account2.balance=}")

allAccounts = [account1, account2]

for i in range(1, 10_001):
    newAccount = BankAccount(f"{i}iban", f"{i}name")
    newAccount.deposit(50)
    allAccounts.append(newAccount)

totalBalances = 0

for account in allAccounts:
    totalBalances += account.balance

print(f"{totalBalances=}")
print(f"{len(allAccounts)=}")
mean = totalBalances / len(allAccounts)
print(f"{mean=}")
