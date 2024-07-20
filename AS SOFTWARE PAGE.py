print(1*'#',100*'.')
a = "Minimum to register yourself as software employee are:"#str
b = "1. need to hold a bachelor's degree"#str
c = "2. need to have atleast 2years of experience"#str
print(a)
print(b)
print(c)
print(100*'#')
d = "The prefered requirements are:"
e = "1. holding a master or phd degree "#str
f = "2. need to have an experience of 4 years"#str
g = "3. relavant skills in required field"#str
print(d)
print(e)
print(f)
print(g)
print(100*'#')
experience = int(input("experience :"))
compaines_worked_for = str(input("compaines you worked for:"))
projects_done = str(input("recent project that you have worked on :"))
skils_learnt = str(input("Skills that have learnt :"))

print("The details that you have mentioned above are :")#str
print("experience :",experience)
print("compaines you have worked for :",compaines_worked_for)
print("recent project that you have worked on :",projects_done)
print("Skills that have learnt :",skils_learnt)

print("if the above mentioned details are correct enter'YES'.")
print("if the above mentioned details are incorrect enter'NO'.")
ans = str(input("enter choice :"))

if ans == "YES":
    print(100*'#')
    print("Registration as a software employee is successfully completed")
    print(100*'#')

if ans == "NO":
   experience = int(input("experience :"))
   compaines_worked_for = str(input("compaines you worked for:"))
   projects_done = str(input("recent project that you have worked on :"))
   skils_learnt = str(input("Skills that have learnt :"))     
   print("The details that you have mentioned above are :")#str
   print("experience :",experience)
   print("compaines you have worked for :",compaines_worked_for)
   print("recent project that you have worked on :",projects_done)
   print("Skills that have learnt :",skils_learnt)

print("if the above mentioned details are correct enter'YES'.")
ans = str(input("enter choice :"))   
print(100*'#')
print("Registration as a software employee is successfully completed")
print(100*'#')