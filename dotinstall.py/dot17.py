# クラス
#　-アクセス制限

class User:
    def __init__(self, name):
        self._name = name
    def say_hi(self):
        print("hi{0}".format(self.name))

tom = User("tom")
print(tom._name)
tom.say_hi()
