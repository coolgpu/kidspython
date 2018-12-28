# calcuate factorial using recursive function
#  give 10, result = 10 * 9 * ... 1;

# 1st do it using for loop
def calcfactorial(n):
    product = 1
    for x in range(1, num + 1):
        product *= x
    return product


num = 3
print("{}! = {}".format(num, calcfactorial(num)))

"""Now we try using recursion function"""
def calcfactorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * calcfactorial_recursive(n-1)

print("{}! = {}".format(num, calcfactorial_recursion(num)))
print("Done")
