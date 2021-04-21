class Bank:
  def __init__(self, name, funds):
    self.name = name
    self.funds = funds
    self.accounts = []
  
  def add_client(self, client):
    self.clients.append(client)

  def __str__(self):
    return 'Bank name: {}, Funds: {}, Number of clients: {}'.format(self.name, self.funds, len(self.accounts))

class _Account:
  def __init__(self, client, bank, funds):
    self.client = client.name
    self.bank = bank.name
    self.funds = funds
    self.credit = 0
    bank.accounts.append(self)
    client.funds -= funds

  def __str__(self):
    return 'Name: {}, Bank: {}, Funds: {}, Credit: {}'.format(self.client, self.bank,                                                    self.funds, self.credit)

class Client:
  def __init__(self, name, funds):
    self.name = name
    self.funds = funds
    self.accounts = []
  
  def __str__(self):
    return 'Name: {}, Funds: {}, Number of accounts: {}'.format(self.name, self.funds, len(self.accounts))

  def print_accounts(self):
    for account in self.accounts:
      print(account)

  def create_account(self, bank, funds):
    self.accounts.append(_Account(self, bank, funds))
  
  def delete_account(self, bank):
    for account in self.accounts:
      if bank.name == account.bank:
        self.accounts.remove(account)
        bank.accounts.remove(account)

  def change_bank(self,old_bank, new_bank):
    for account in self.accounts:
      if old_bank.name == account.bank:
        self.create_account(new_bank, account.funds)
        self.delete_account(old_bank)

  def money_deposit(self, bank_name, money):
    if money < self.funds:
      for account in self.accounts:
        if bank_name == account.bank:
          account.funds += money
          self.funds -= money

  def money_withdraw(self, bank_name, money):
    for account in self.accounts:
      if bank_name == account.bank:
        if money < account.funds:
          account.funds -= money
          self.funds += money

  
  def momey_transfer(self, bank_name, money, person, person_bank_name):
    for account in self.accounts:
      if bank_name == account.bank:
        if money < account.funds:
          for account_person in person.accounts:
            if person_bank_name == account_person.bank:
              account.funds -= money
              account_person.funds +=money


  def credit(self, bank, money):
    for account in self.accounts:
      if bank.name == account.bank:
        if money < bank.funds:
          bank.funds -= money
          account.credit += money


if __name__== "__main__":
  bank1 = Bank('PKO', 1000000)
  bank2 = Bank('PEKAO', 1000000)
  print(bank1)
  person1 = Client('John Doe', 10000)
  person2 = Client('Jane Scott', 5000)
  print(person1)
  person1.create_account(bank1,100)
  person2.create_account(bank1,200)
  print(bank1)
  print(person1)
  person1.print_accounts()
  person1.money_deposit('PKO', 20)
  person1.print_accounts()
  person1.money_withdraw('PKO', 50)
  print(person1)
  person1.print_accounts()
  person1.momey_transfer('PKO', 10, person2, 'PKO')
  person1.print_accounts()
  person2.print_accounts()
  print(person1)
  print(bank1)
  person1.credit(bank1, 1000)
  print(bank1)
  person1.print_accounts()
  person1.change_bank(bank1,bank2)
  print(bank1)
  print(bank2)
  person1.print_accounts()