print(1*'#',100*'.')
hd = "AS"
c = hd.center(90)
print(c)

#str
a = ("hello guys welocome to the website. This website helps you earn and eduacate yourself by enrolling yourself here")
print(a)

#user OPT
print("press S to register as software")
print("press T to register as teacher")

ans = str(input("enter your choice"))

if ans == "S":
    print(50*'#')
    print(a)
    name = input("Enter your name :")
    dob = input("Enter your date of birth (DD-MM-YYYY) :")
    phonenumber = int(input("Enter your mobile number :"))
    education_qualification = input("Enter your highest educational qualification :")
    experience = int(input("Enter your years of experience :"))

if ans == "T":
    print(50*'.')
    print(a)
    name = input("Enter your name :")
    dob= input("Enter your date of birth (DD/MM/YYYY):")
    phonenumber = int(input("Enter your phone number :"))
    education_qualification = input("Enter your highest educational qualification :")
    experience = int(input("Enter yor years of experience"))

b =(10*'.')
b =(10*'.')
print(b)

print("The details you mentioned above")
print("name :" ,name )
print("Date of birth :",dob[0],dob[1],"/",dob[2],dob[3],"/",dob[4],dob[5],dob[6],dob[7])
print("phone number :",phonenumber)
print("education qualification",education_qualification)
print("experience :",experience)


print("if the details mentioned above you are correct then enter YES and click enter")
print ("if any changes required then press NO and click enter")

ans = str(input("Enter your choice :"))

if ans == "YES": 
  print(b)
  print(b)
  d = "Registration successfully completed" #str
  print(d)
 
if ans == "NO":
  print(b)
  e = "Registration unsuccessfully.Please try again"
  print(e)
  name = input("Enter your name :")
  dob = input("Enter your date of birth (DD-MM-YYYY) :")
  phonenumber = int(input("Enter your mobile number :"))
  education_qualification = input("Enter your highest educational qualification :")
  experience = int(input("Enter your years of experience :"))
  print("if the details mentioned above arer correct?")
  ans = str(input("Enter your choice :"))

if ans == "YES": 
  print(b)
  print(b)
  f = "Registration successful."
  print(f)
  A = (100*'.')
  print(A)
  print(A)