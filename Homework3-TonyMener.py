# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:31:50 2019

@author: Nurhan Mener

"""
#Exercise 1 on Page 62
#set Variables to Zero
total=0
count=0

#set up WHile Loop
while True:
    entval = input('Enter a Number ')
    
    
#Set Break when Done is entered    
    
    if entval == 'done':
        break
#Test the values entered are valid
    try:
        fltentval = float(entval)
    except:
        print('Invalid input')
        continue
    
#Add values to toal, count    
    total = total + fltentval
    count = count + 1

    
#Return that the code is complete and return total, count and average    
print('Done')
print(total, count, total/count)  

  

    

#Exercise 5.2 on Page 63


# creating an empty list 

lst = [] 
  
# number of elemetns as input 
while True:
    entval = input('Enter a Number ')
    
    
#Set Break when Done is entered    
    
    if entval == 'done':
        lst.sort()
        print("Largest element is:", lst[-1])
        print("Smallest element is:", *lst[:1])
        break
#Test the values entered are valid
    try:
        fltentval = float(entval)
    except:
        print('Invalid input')
        continue
  
 
  
    lst.append(fltentval) # adding the element 
    
    
#Ch6 Ex 4  PG71
    
 

str = "bananas"
sub = 'a'
print ("str.count('a') : ", str.count(sub))

#Ch6 Ex 5  PG75

text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find(' ')
#print(atpos)
sppos = text[atpos:]
#print(sppos)
sppos.strip()
print(float(sppos))



#