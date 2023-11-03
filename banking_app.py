#Parent class: User

class User():
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def show_user_details(self):
    print("Personal Details: ")
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
    print("Account balance has been updated : ", self.balance)
  
  

# john = User('Johan', 21, 'Male')
# john.show_user_details()

# johan = Bank('Johan', 40, "Male")
# johan.name

jonny = Bank('jonny', 30,'Male')
jonny.deposit(200)
jonny.deposit(500)