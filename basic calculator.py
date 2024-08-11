print("#"*100)
aa = "CALCULATOR"
head = aa.center(90)
print(head)
print("#"*100)
print("This is basic calculator")
bb = '''This can do both normal and decimal type
1. normal
2. decimal'''
cal = input("Enter your choice :")
cal = cal.lower()
if cal == "normal":
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
 elif opt =="division" :
    b = int(input("Enter a value :"))
    c = int(input("Enter b value :"))
    print("a / b :",b/c)
 else :
    print('''The feature is isn't avaiable in our calculator
          try again''')
 print("THANKS FOR USING CALCULATOR")
else :
    print(''' This calculator provides basic operations :
      1. addition
      2. subtration
      3. multiplication
      4. division''')
opt = input("Enter the opertion that you like to perform :")
opt = opt.lower()
if opt == "addition" :
    a = float(input("Enter a value :"))
    b = float(input("Enter b value :"))
    print("a + b :",a+b)
elif opt == "subtration" :
    a = float(input("Enter a value :"))
    b = float(input("Enter b value :"))
    print("a - b :",a-b)
elif opt == "multiplication" :
    a = float(input("Enter a value :"))
    b = float(input("Enter b value :"))
    print("a * b :",a*b)
elif opt == "division" :
    a = float(input("Enter a value :"))
    b = float(input("Enter b value :"))
    print("a / b",a/b)
else :
    print('''It seems you have entered the inncorrect operation
          Please restart the calculator again.''')
print("Thanks for using the calculator.")
           