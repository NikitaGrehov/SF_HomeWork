class User():
    def __init__(self, email, password, balance):
        self.email=email
        self.password=password
        self.balance=balance
        update_balance=0
     
    def login(self, email, password):
        if self.email==email and self.password==password:
            answer=True
        else:
            answer=False
        return answer
    
    def update_balance(self, amount):
        self.balance+=amount
        return self.balance 
user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")
# => False
user.login("gosha@roskino.org", "qwerty")
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700
# => Average department revenue for Danon: 700000