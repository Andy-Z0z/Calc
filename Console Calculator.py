#The calculator.
print("Hello! Welcome to Console Calculator!")

#Variables
a = float(input("First number: "))
b = float(input("Second number: "))
c = input ("Operation: (+ - * / ** % //): ")

#Operations

if c == "+": #+
    d = a+b
    print("Your result is:", d, type(d))


if c == "-": #-
    d = a-b
    print("Your result is:", d, type(d))
           
if c == "/": #/
    d = a/b
    print("Your result is:", d, type(d))

if c == "*": #*
    d = a*b
    print("Your result is:", d, type(d))

if c == "**": #**
    d = a**b
    print("Your result is:", d, type(d))

if c == "%": #%
    d = a%b
    print("Your result is:", d, type(d))

if c == "//": #//
    d = a//b
    print("Your result is:", d, type(d))

