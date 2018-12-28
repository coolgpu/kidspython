import datetime

def printmorning():
    print("Good morning!")


today = datetime.datetime.today()
name = "Xiyun"
age = 40
print("Hellow World, %s. And I am %d years old, and my favorite number is %.1f" % (name, age, 3.14))
print("Hello World!", name)
print("Today is ", today)
print("Today is ", today.strftime("%A"))
printmorning()
