
from breezypythongui import EasyFrame
from bank import Bank,SavingsAccount

def main(fileName = None):
    bank = Bank()
    bank.add(SavingsAccount("Wilma", "1001", 4000.00))
    bank.add(SavingsAccount("Fred", "1002", 1000.00))
    
if __name__ == "__main__":
    main()

class ATM(EasyFrame):
    def __init__(self, bank):
        EasyFrame.__init__(self, title = "ATM")
        self.bank = bank
        self.account = None
    def login(self):
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.account:
            self.statusField.setText("Hello, " + name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.loginButton["text"] = "Logout"
            self.loginButton["command"] = self.logout
        else:
            self.statusField.setText("Name and pin not found!")
    
    def logout(self):
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Welcome to the Bank!")
        self.balanceButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.loginButton["text"] = "Login"
        self.loginButton["command"] = self.login
    
    def getBalance(self):
        balance = self.account.getBalance()
        self.statusField.setText("Balance: $" + str(balance))
    
    def withdraw(self):

        amount = self.amountField.getNumber()
        message = self.account.withdraw(amount)
        if message:
            self.statusField.setText(message)
        else:
            self.statusField.setText("Withdrawal successful!")