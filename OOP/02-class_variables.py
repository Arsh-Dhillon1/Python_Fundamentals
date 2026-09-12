class User:
    joining_year = 2026
    count_users = 0

    def __init__(self,name,id):
        self.name = name
        self.id = id
        User.count_users+=1


user1 = User("Arsh",1)

print(user1.name)
print(user1.joining_year)
print(User.joining_year)

print(User.count_users)