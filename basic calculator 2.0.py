print("#"*100)
aa = "CALCULATOR"
head = aa.center(90)
print(head)
print("#"*100)
print("This is basic calculator")
cc = '''This calculator provides operations like : 
 1. addition
 2. subtraction
 3. multiplication
 4. division'''
print(cc)
opt = input("enter the type of operations do you want to :") #sting
opt = opt.lower()
if opt == "addition" :
    b = int(input("Enter a value :"))
    c = int(input("Enter b value :"))
    print("a + b :",b+c)
elif opt == "subtraction" :
    b = int(input("Enter a value :"))
    c = int(input("Enter b value :"))
    print("a - b :",b-c)
elif opt == "multiplication" :
    b = int(input("Enter a value :"))
    c = int(input("Enter b value :"))
    print("a * b :",b*c)
elif opt == "division":
    b = int(input("Enter a value :"))
    c = int(input("Enter b value :"))
    if c == 0:  # Check if c is zero
        print("error can't divide by zero")
    elif b == 0: #check if b is zero
        print("error can't divide by zero")
    else:
        print("a / b :", b / c)
else:
    print('''The feature isn't available in our calculator
          try again''')
print("THANKS FOR USING CALCULATOR")