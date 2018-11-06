# クラス
#　-アクセス制限

class User:
   def __init__(self, name):
     self.__name = name
   def say_hi(self):
     print("hi {0}".format(self.__name))

tom = User("tom")
print(tom.__name)
tom.say_hi()
