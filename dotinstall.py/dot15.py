# クラス

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name

print(User.count) # 0
tom = User("tom")
bob = User("bob")
print(User.count) # 0

print(User.count) # 2
