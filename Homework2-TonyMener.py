# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:31:50 2019

@author: Nurhan Mener

"""
#Exercise 2 on Page 38
Hours = input('Enter the Number of Hours worked ')
Rate = input('Enter the Rate of Pay ')
try:
    pay = int(Hours)*int(Rate)
    print('Pay:' , pay)
except:
    print('Please Enter a number')



#Excercise 3 on Page 38 & 39
Grade = input('Enter a Score ')
try:
    Grade = float(Grade)    
    if Grade > 1  or Grade < 0:
        print('Bad score')
    elif Grade >= .9:
        print('A')
    elif Grade >= .8:
        print('B')
    elif Grade >= .7:
        print('C')
    elif Grade >= .6:
        print('D')
    else:
        print('F')
except:
    print('Bad score')


#Excercise 6 on Page 52 & 53
    
def computepay(Hrs,Rt): 
    if Hrs <= 40 and Hrs >= 0:
        pay = Hrs*Rt

    else:
        pay = (Hrs-40)*(Rt*1.5) +  (40*(Rt))
    return pay
    
    
    
Hours = input('Enter Hours: ')
Hrs = float(Hours)
Rate = input('Enter Pay ')
Rt = float(Rate)

if Hrs and Rt > 0:
    p = computepay(Hrs,Rt)
    print('Pay: ', p)

    
else:
    print('Invalid Entry to calculate pay')


