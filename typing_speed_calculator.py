from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if(partest[i]!=usertest[i]):
                error = error +1
        except:
            error = error + 1
    return error

def speed_test(test1,test2,usertest):
    time_delay = test2 - test1
    time_r = round(time_delay,2)
    speed = len(usertest)/time_r
    return round(speed,2)

test = ["Tanmay is from jalgaon","He studies is I2it hinjawadi","preparing for gate in ace academy"]
test1 = r.choice(test)
print()
print(test1)
print()
print("-----speed test-----\n\n")

time_1 = time()
user_test = input()
time_2 = time()

print("\n\n")

print("time required is    :",speed_test(time_1,time_2,user_test))
print()
print("errors occured are   :",mistake(test1,user_test))

