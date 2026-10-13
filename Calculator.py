def add(a, b):
    answer=a +b
    print(str(a)+ " + " + str(b) +  " = " + str(answer))

def sub(a, b):
    answer= a-b
    print( str(a)+ " - " + " b " + " = " + str(answer))

def mul(a, b):
    answer= a*b
    print( str(a)+ " * " + " b " + " = " + str(answer))

def div(a, b):
    answer= a/b
    print( str(a)+ " / " + " b " + " = " + str(answer))  

while True:
    print ("A, Addition")
    print ("B, Substraction") 
    print ("C, Multipliction")
    print ("D, Division")
    print ("E, Exit")

    choice= input("Input your choice: ")
    if choice== "a" or choice== "A":
        print ("Addition")
        a=input("input first number: ")
        b=input("input second number: ")
        add(a,b)

    elif choice== "B" or choice=="b":
        print ("substraction")
        a=input("input first number: ")
        b=input("input second number: ")
        sub(a,b)

    elif choice== "c" or choice==  "C":
        print ("Multiplication")
        a=input("input first number: ")
        b=input("input second number: ")
        mul(a,b)

    elif choice== "d" or choice==  "D":
        print ("Division")
        a=input("input first number: ")
        b=input("input second number: ")
        div(a,b)

    elif choice== "e" or choice==  "E":
        print ("program ended")
        quit()
        