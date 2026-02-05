from personal_account import PersonalAccount

def test_deposit():
    account = PersonalAccount(1, "Alice")
    account.deposit(100)
    assert account.get_balance() == 100

def test_withdraw():
    account = PersonalAccount(2, "Bob")
    account.deposit(200)
    account.withdraw(50)
    assert account.get_balance() == 150

def test_insufficient_balance():
    account = PersonalAccount(3, "Charlie")
    account.deposit(100)
    try:
        account.withdraw(200)
    except ValueError:
        assert True
