
class Bank:
  def __init__(self, name):
    self.name = name
    self.clients = []
  
  def add_client(self, client):
    self.clients.append(client)

class Client:
  def __init__(self, name, money):
    self.name = name
    self.money = money

  def __str__(self):
    return '{} has {} money.'.format(self.name, self.money)

class Transfer:
  def __init__(self, name):
    self.name = name

  def money_transfer(self, money, client):
    if self.name == 'income':
      client.money += money
    if self.name == 'outcome':
      client.money -= money

if __name__== "__main__":
  bank = Bank('first_bank')
  print(bank.name)
  client = Client('Jane', 100)
  print(client.name)
  print(client.money)
  bank.add_client(client)
  print(bank.clients[0].name)
  transfer = Transfer('income')
  transfer.money_transfer(100, client)
  print(client)
