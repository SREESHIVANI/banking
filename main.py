class User():
    def __init__(self, name, age, gender, phno):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phno

    def show(self):
        print("Personal details")
        print(" ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Phone number:", self.phone_number)


a = User("Amit", 34, "Male", 987456321)
a.show()
class Bank(User):
    def __init__(self,name,age,gender,phno):
        super(). __init__(name,age,gender,phno)
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+amount
        print("Account balance has been updated: Rs",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient balance: Rs", self.balance)
        else:
            self.balance=self.balance-self.amount
            print("successful withdrawn and updated balance is: Rs",self.balance)
    def view_balance(self):
        self.show()
        print("Updated balance is : Rs",self.balance)
anil=Bank("Anil",26,"Male",9874563210)
anil.deposit(10000)
anil.withdraw(11000)
anil.view_balance()