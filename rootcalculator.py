print('#'*100)
a = 'Welcome to root calculator'
b = a.center(100)
print(b)
c = '''HERE, You needto understand how to use a root calculator
 let's us consider a equation ax^2+bx+c = 0
 here you need to substitute the coefficent of a , b ,c.
 Then we calculate the values and we will give you the roots.
 Note : this a basic root calculator where this is useful for quadratic equations.'''
print(c)
e = int(input("Enter the coefficient of x^2 :"))
f = int(input("Enter the coeffiecent of x :"))
g = int(input("Enter the constant :"))
print(f"The input you have given are : {e},{f},{g}")
ans = input('''Do you want to continue with this input
          click yes to continue or no to restart''')
if ans == 'yes' :
 root1 = 0 #consider root1 as zero we will later change it
 root2 = 0 #consider root2 as zero we will later change it
 d = f**2 - 4*e*g
 if d >= 0:
  root1 = (-f+(d**(0.5)))/2*e
  root2 = (-f-(d**(0.5)))/2*e
  print("The roots of the equation are :")
  print(root1)
  print(root2)
 else:
  realpart = -f/(2*e)
  imgpart = (abs(d)**(0.5))/(2*e)
  print("The roots of the equation are :")
  print(f"{realpart} + {imgpart}i")
  print(f"{realpart} - {imgpart}i")
  t = 'THANK YOU'
  tq = t.center(100)
  print(tq)
  print('#'*100)
if ans == 'no':
 t = 'THANK YOU'
 tq = t.center(100)
 print(tq)
 print('#'*100)