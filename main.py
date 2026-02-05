from personal_account import PersonalAccount

account = PersonalAccount(1001, "John Doe")

account.deposit(500)
account.withdraw(150)

account + 200      # using __add__
account - 100      # using __sub__

print(account)
print()
account.print_transaction_history()
print()
print("Current Balance:", account.get_balance())
