# There is a bank, giving you a APR 6% for your saving account. If you have $1 at the beginning. Please use
# use python to calculate how much you will have after 12 years
import math

# (1 + Apr) ** N
# another comment
apr = 0.06
init = 1.0
sum = (1.0 + apr) ** 12
print("The total will be %f" % sum)

sum1 = 1.0
for y in range(1,13):
    sum1 *= (1.0 + apr)
print("sum1 from for loop is %f" % sum1)



# Another banker, giving a rate based on the number of years. For N year, the rate is 1/N
# for example, for 100 years, the rate is 1/100
numyears = 1000
years = range(1,numyears + 1)
# apr = 1.0/numyears
# sum1 = 1.0
for y in years:
    apr = 1/y
    balance = (1.0 + 1/y)**y
    print("After year %d, value is %f" % (y, balance))

# now directly calculate constant e:
# definition of e: (1+1/N) ^ N
print("math.e = %f" % math.e)

