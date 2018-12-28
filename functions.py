def function1():
    print("my python function!")
    return "Good "

newstring = function1() * 2
print(newstring)

def addfunction(a,b):
    return a+b


def printname(score, s = "NoName"):
    print("The name is %s and score is %d" % (s, score))
    return




name = "Xiyun Song"
printname(90)

c = addfunction(5, 9)
print("the sum is %d" % c)
