#Parent class: User

class User():
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def show_user_details(self):
    print("Personal Details:")
    print("")
    print("Name  ", self.name)
    print("Age  ", self.age)
    print("Gender  ", self.gender)

#Child Class
class Bank(User):
  def __init__(self, name, age, gender):
    super().__init__(name, age, gender)
    self.balance = 0
  
  def deposit (self,amount):
    self.amount = amount
    self.balance = self.balance + self.amount
    print("Account balance has been updated : $", self.balance)
  
  def withdraw(self, amount):
    self.amount = amount
    if(self.amount > self.balance):
      print("Insufficient Funds | Balance Available : $", self.balance)
    else:
      self.balance = self.balance - self.amount
      print("Account balance has been updated :$", self.balance)
  
  def view_balance(self):
    self.show_user_details()
    print("Account balance is: $", self.balance)
  
johnny = Bank('jonny', 30,'Male')
johnny.deposit(200)
johnny.deposit(500)
johnny.withdraw(700)
johnny.view_balance()