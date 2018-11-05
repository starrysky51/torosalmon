# 関数

#def say_hi():
#    print("hi")
#
#say_hi()

def say_hi(name, age = 20):
    print("hi {0} ({1})".format(name,age))

say_hi("tom", 23) # tom(23)
say_hi("bob", 21) # bob(21)
say_hi("steve")   # steve(20)
say_hi(age = 18, name = "rick")
