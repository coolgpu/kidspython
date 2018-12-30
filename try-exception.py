# example 1
# print(x)
try:
    # This statement will raise an error, because x is not defined:
    print(x)
except:
    print("An exception occurred")

# Example 2: Print one message if the try block raises a NameError and another for other errors:
try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")



# example 3: You can use the "else" eyword to define a block of code to be executed if no errors were raised:
try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

# example 4: The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")
finally:
    print("This block will be executed regardless if the try block raises an error or not")

# Useful when Try to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
else:
    f.close()
finally:
    print("This block will be executed regardless if the try block raises an error or not")




# 10 * (1/0) # This statement will cause crash
try:
    10 * (1 / 0)
except ZeroDivisionError:
    print("Error: division by zero")
except:
    print("something wrong")

# '2' + 2 # This statement will cause crash
try:
    '2' + 2
except TypeError:
    print("Error: Can't convert 'int' object to str implicitly")
except:
    print("something wrong")

while True:
    try:
        v =  int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number. Try again...")
    except:
        print("Something went wrong when writing to the file. Try again...")
    else:
        print("The value is {}".format(v))
    finally:
        print("This block will be executed regardless if the try block raises an error or not")


# '2' + 2 # This statement will cause crash
try:
    '2' + 2
except (RuntimeError, TypeError, NameError):
    pass
except:
    print("something wrong")
finally:
    print("Finally")


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
    print("After 'raise'")
