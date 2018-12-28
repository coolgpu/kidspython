def testarguments_int(a):
    print("before increment id(a)= %d" % id(a))
    a += 1
    print("after increment id(a)= %d" % id(a))

num = 9

print("id(num)= %d" % id(num))
print("before call function, num= %d" % num)
testarguments_int(num)
print("id(num)= %d" % id(num))
print("after call function, num= %d" % num)

def testarguments_list(b):
    print("before increment id(b)= %s" % id(b))
    b.append("Good morning")
    print("after increment id(b)= %d" % id(b))

mylist = ["apple", 67]

print("id(mylist)= %d" % id(mylist))
print("before call function, mylist=", mylist)
testarguments_list(mylist)
print("id(mylist)= %d" % id(mylist))
print("after call function, mylist=", mylist)

