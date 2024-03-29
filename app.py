def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def divide(x,y):
    return (x/y)

print("select calculation")
print("select 1 for add")
print("selct 2 to subtract")
print("select 3 to multiply")
print("select 4 to divide")
print("select 5 to end")
runstate = True


while runstate == True:
   
    choice = input("select (1/2/3/4): ")




    if choice in ('1','2','3','4'):

        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid Input. Enter a number")



    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
      print(num1, "x", num2, "=", multiply(num1. num2))

    elif choice == '4':
        try:
            print(num1, "/", num2, "=", divide(num1,num2))
        except ZeroDivisionError:
           print("Cannot divide by 0")
    
    else:
        print("Ended")
        runstate = False
           
    

   



    