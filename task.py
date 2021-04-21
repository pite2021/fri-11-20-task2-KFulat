import random
from dataclasses import dataclass

class Bank:
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.accounts = []

    def add_client(self, client):
        self.clients.append(client)

    def __str__(self):
        return 'Bank name: {}, Funds: {}, Number of clients: {}'.format(
            self.name, self.funds, len(self.accounts))

class _Account:
    def __init__(self, client, bank, funds):
        self.client = client.name
        self.bank = bank.name
        self.funds = funds
        self.credit = 0
        bank.accounts.append(self)
        client.funds -= funds

    def __str__(self):
        return 'Name: {}, Bank: {}, Funds: {}, Credit: {}'.format(
            self.client, self.bank, self.funds, self.credit)


class Client:
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.accounts = []

    def __str__(self):
        return 'Name: {}, Funds: {}, Number of accounts: {}'.format(
            self.name, self.funds, len(self.accounts))

    def print_accounts(self):
        str = '{} accounts:'.format(self.name)
        for account in self.accounts:
            str = '{}\n{}'.format(str, account)
        return str

    def create_account(self, bank, funds):
        self.accounts.append(_Account(self, bank, funds))

    def delete_account(self, bank):
        for account in self.accounts:
            if bank.name == account.bank:
                self.accounts.remove(account)
                bank.accounts.remove(account)

    def change_bank(self, old_bank, new_bank):
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
                            account_person.funds += money

    def credit(self, bank, money):
        for account in self.accounts:
            if bank.name == account.bank:
                if money < bank.funds:
                    bank.funds -= money
                    account.credit += money


if __name__ == "__main__":

    bank1 = Bank('PKO', funds=1000000)
    bank2 = Bank('PEKAO', funds=1000000)
    bank3 = Bank('SANTANDER', funds=2000000)
    banks = [bank1, bank2, bank3]

    persons = []
    persons_names = [
        'John Doe', 'Jane Austin', 'Romuald Tolkien', 'Paul Dirac',
        'Enrico Fermi', 'Bon Jovi', 'Eric Clapton', 'Sasha Grey',
        'Michelle Obama', 'Marie Curie', 'Emmy Noether', 'Ray Charles'
    ]
    init_funds = 2000
    init_money_bank = 100
    for person_name in persons_names:
        client = Client(person_name, init_funds)
        persons.append(client)
        client.create_account(random.choice(banks), init_money_bank)
    print(bank1)
    print(bank2)
    print(bank3)

    print(persons[0])
    print(persons[0].print_accounts())
    persons[0].create_account(bank2, 200)
    print(persons[0].print_accounts())
    persons[0].money_deposit('PEKAO', 100)
    print(persons[0].print_accounts())
    persons[0].money_withdraw('PEKAO', 50)
    print(persons[0].print_accounts())
    persons[1].create_account(bank2, 200)
    print(persons[1].print_accounts())
    persons[0].momey_transfer('PEKAO', 20, persons[1], 'PEKAO')
    print(persons[0].print_accounts())
    print(persons[1].print_accounts())
    persons[0].change_bank(bank2, bank1)
    print(persons[0].print_accounts())
    print(bank1)
    persons[0].delete_account(bank1)
    print(persons[0].print_accounts())
    print(bank1)
