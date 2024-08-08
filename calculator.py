print(100*'#')
hd = "CALCULATOR"
a = hd.center(90)
print(a)
mb = "It is just a basic calculator of AMSD of two numbers"
x = mb.center(90)
print(x)
print(100*'#')

abc = "which type of calculation do you want to perform :"
bbc = "1. normal "
cbc = "2. decimal"
print(bbc)
print(cbc)
eee = str(input("ENTER YOUR CHOICE :"))
eee = eee.lower()
if eee == "normal":

 b = "Which calculation do you want to perform?"
 c = "1. addition"
 d = "2. multipilcation"
 e = "3. subtraction"
 f = "4. division"
 print(b)
 print(c)
 print(d)
 print(e)
 print(f)
 ans = str(input("ENTER YOUR CHOICE :"))
 ans = ans.lower()

 if ans == "addition":
    a = int(input("ENTER FIRST VALUE :"))
    b = int(input("ENTER SECOND VALUE :"))
    print(a+b)
 if ans ==  "multiplication":
    a = int(input("ENTER FIRST VALUE :"))
    b = int(input("ENTER SECOND VALUE :"))
    print(a*b)
 if ans == "subtraction":
    a = int(input("ENTER FIRST VALUE :"))
    b = int(input("ENTER SECOND VALUE :"))
    print(a-b)
 if ans == "division":
    a = int(input("ENTER FIRST VALUE :"))
    b = int(input("ENTER SECOND VALUE :"))
    print(a/b)  
 print("THANKS FOR USING CALCULATOR")    

if eee == "decimal":
 a = "1. addition"
 b = "2. multiplication"
 c = "3. subtraction"
 d = "4. division"
 print(a)
 print(b)
 print(c)
 print(d)
 ans = str(input("ENTER YOUR CHOICE :"))
 ans = ans.lower()
 if ans == "addition":
    e = float(input("ENTER FIRST VALUE :" ))
    f = float(input("ENTER SECOND VALUE :"))
    g = e + f
    print(g)
 if ans == "multiplication":
    e = float(input("ENTER FIRST VALUE :" ))
    f = float(input("ENTER SECOND VALUE :"))
    g = e * f
    print(g) 
 if ans == "subtraction":
    e = float(input("ENTER FIRST VALUE :" ))
    f = float(input("ENTER SECOND VALUE :"))
    g = e - f
    print(g)    
 if ans == "division":
    e = float(input("ENTER FIRST VALUE :" ))
    f = float(input("ENTER SECOND VALUE :"))
    g = e / f
    print(g)
 print("THANKS FOR USING THE CALCULATOR")
