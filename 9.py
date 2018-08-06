#!/usr/bin/python

number = 0

while(number<100):
    if(number%2 == 0 and number <10):
        print(' ' + str(number),end='')
    elif(number%2 == 0):
        print(number,end='')
    if(number>0 and number%10 == 8):
        print('\n')
    number = number +1