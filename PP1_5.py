'''
    Lesson: Typecasting
    Author: Eric Fang
    Date Created: September 23rd, 2024
    Date Last Modified: September 24th, 2024
'''

import math

def q1():
  #Write Assignment code here
  num = input("Input an integer: ")
  num = int(num)
  num = num + 3
  print(num)

def q2():
  #Write Assignment code here
  num = input("Input a number: ")
  num = num + "4"
  num = float(num) + 2
  print(num)

def q3():
  #Write Assignment code here
  radius = float(input("Input a radius: "))
  print(math.pow(radius, 2) * 3.14)

def q4():
  #Write Assignment code here
  num = float(input("Input a number: "))
  num = num * 12
  num = int(num)
  print(num)  

def q5():
  #Write Assignment code here
  num = int(input("Input an integer: ")) + 5
  print(f"Your number + 5 is {num}")

#Comment this code out when running tests
#Do not comment this out when running your program normally

'''
q1()
q2()
q3()
q4()
q5()
'''
