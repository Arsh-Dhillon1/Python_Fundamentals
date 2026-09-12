class User:
    def __init__(self,name,id,email,phone):
        self.__name = name
        self.id = id
        self.email = email
        self.phone = phone
    def get_mail(self):
        print(f"The email of customer is: {self.email}")

    def update_mail(self,new_mail):
        self.email = new_mail
        print("Email Successfully Changed!!")

user1 = User("Arsh Dhillon", 1, "arshdhillon2094@gmail.com","+91-7009430005")
print(user1._User__name)
print(user1.id)
print(user1.email)
print(user1.phone)
user1.get_mail()
user1.update_mail("arshdhillon2000@gmail.com")
user1.get_mail()

print()

user2 = User("Bonzo Dhillon", 2, "bonzo@gmail.com", "+91-9109106700")

print(user2._User__name)
print(user2.id)
print(user2.email)
print(user2.phone)

user2._User__name = "DJ Bonzo"

print(user2._User__name)