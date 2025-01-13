def add(x,y):
    return y + x

def sub(x,y):
    return x - y

def multi(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Welcome to my calculator")
print("1 for add")
print("2 for sub")
print("3 for multi")
print("4 for divide")
while True:
    choice_input=input("Enter your choice")
    if choice_input in ("1","2","3","4"):

        try:
            num_1 = float(input("Enter first number"))
            num_2 = float(input("Enter second number"))
        except ValueError:
            print("wrong format")
            continue
        
        if choice_input == "1":
            print (num_1,"+",num_2,"=",add(num_1,num_2))
        elif choice_input =="2":
            print (num_1,"-",num_2,"=",sub(num_1,num_2))
        elif choice_input == "3":
            print (num_1,"x",num_2,"=",multi(num_1,num_2))
        elif choice_input =="4":
            print (num_1,"/",num_2,"=",divide(num_1,num_2))
        


    
