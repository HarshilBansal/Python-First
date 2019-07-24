#Main Editor File......
#Single line comments
#Input Output
#output ----- print()
s = '''print(123123,end=',')

print(123.234,end=',')
print('A')
print("String");
print("Hey","Hello",123.12,456,sep='----');
print("*********************")
#by default, print will take cursor to next line
#To change this behavior, use 'end' attribute
print(123)
print(3123123)
#----------------------------------------------------
#inputs

#print(input())
#Python is a dynamically data typed language
x = 9.876
y = 6752
z = 762723576253746527342364526345762354762534765237465273645276354762354*8
print(z)
print(type(x))
#variable ---- declaration, definition
#In Dynamically Data Typed Language, no syntax for declaration of a variable
#Data Types----- 2 data types and 4 data structures are given here
#1. Number ---- integer, real, double, long,complex etc..
#2. String ---- ''/""/''' '''/""" """#Ascci Table
st1 = '61257351276357123'
st2 = "234234234"
print(type(st2))
'''
print(23+45)
########Input
#input()
#print(s)
x = int(input("Enter Something: "))
#print("You Entered: ",x)
y = float(input("Enter Again: "))
print(type(x),type(y))
print((x)+(y))
#By default, input() will recieve everything as a string, so we have to typecast the values

#eval() ---- 2 things, 1. Type of numeric data,2. SOlve a string expression
x = eval(input("Enter A Number: "))
y = eval(input("Enter Again: "))
print(type(x))
print(x+y)


print(int(45.5))
n = input("Enter Some mathematical expression: ")
print(eval(n))
print(eval('234-90'))




































