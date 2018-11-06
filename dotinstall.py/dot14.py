# クラス

class User:
    def __init__(self, name):
        # インスタンス変数
        self.name = name

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
