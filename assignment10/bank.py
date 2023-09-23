class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def add_account(self, name, account_type, balance, cnic):
        is_exist = False
        for account in self.accounts:
            if account.cnic == cnic:
                is_exist = True
                break
        if (is_exist):
            print("Account already exist with the given CNIC")
        else:
            account = Account(name, account_type, balance, cnic)
            self.accounts.append(account)
    
    def update_account(self, account_id, name=None, account_type=None, balance=None, cnic=None):
        is_exist = False
        for i in range(len(self.accounts)):
            if (self.accounts[i].id == account_id):
                self.accounts[i].update(name, account_type, balance, cnic)
                is_exist = True
                break
        if (not(is_exist)):
            print()
    
    def remove_account(self, id):
        is_exist = False
        for i in range(len(self.accounts)):
            if (self.accounts[i].id == id):
                self.accounts.pop(i)
                is_exist = True
                break
        if (not(is_exist)):
            print("Invalid Account Id")

    def add_money(self, account_id, amount):
        is_exist = False
        for i in range(len(self.accounts)):
            if (self.accounts[i].id == account_id):
                self.accounts[i].add_money(amount)
                is_exist = True
                break
        if (not(is_exist)):
            print("Invalid Account Id")
    
    def remove_money(self, account_id, amount):
        is_exist = False
        for i in range(len(self.accounts)):
            if (self.accounts[i].id == account_id):
                self.accounts[i].remove_money(amount)
                is_exist = True
                break
        if (not(is_exist)):
            print("Invalid Account Id")

    def account_detail(self, account_id):
        is_exist = False
        for i in range(len(self.accounts)):
            if (self.accounts[i].id == account_id):
                print(self.accounts[i])
                is_exist = True
                break
        if (not(is_exist)):
            print("Invalid Account Id")

class Account:
    count = 0
    def __init__(self, name, account_type, balance, cnic):
        Account.count += 1
        self.id = Account.count
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.cnic = cnic

    def add_money(self, amount):
        self.balance += amount

    def remove_money(self, amount):
        if (self.balance - amount) < 0:
            print("No enough balance")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account(id={self.id}, name={self.name}, CNIC={self.cnic}, account_type={self.account_type}, balance={self.balance})"

    def update(self, name, account_type, balance, cnic):
        self.name = name if name != None else self.name
        self.account_type = account_type if account_type != None else self.account_type
        self.balance = balance if balance != None else self.balance
        self.cnic = cnic if cnic != None else self.cnic

bank = Bank("Meezan Bank", "Karachi")
bank.add_account("XYZ", "Asan Account", 0, "42000-0000000-0")
bank.add_account("XYZ", "Asan Account", 0, "42000-0000000-0")
bank.add_money(1, 4000)
bank.remove_money(1, 1500)
bank.account_detail(1)
bank.remove_money(1, 3000)
bank.remove_account(3)
bank.update_account(1, "Huzaifa")
bank.account_detail(1)
bank.remove_account(1)
bank.account_detail(1)
