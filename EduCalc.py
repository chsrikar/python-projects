print('#' * 100)

# Title centered
title = 'Welcome to Root Calculator'
print(title.center(100))

# Description
description = '''\nHERE, you need to understand how to use a root calculator.
Let us consider an equation: ax^2 + bx + c = 0.
You need to substitute the coefficients for a, b, and c.
Then we calculate the values and give you the roots.

Note: This is a basic root calculator, useful for quadratic equations.\n'''
print(description)

# Input
e = int(input("Enter the coefficient of x^2 (a): "))
f = int(input("Enter the coefficient of x (b): "))
g = int(input("Enter the constant term (c): "))
print(f"\nThe input you have given is: a = {e}, b = {f}, c = {g}")

# Confirmation
ans = input("\nDo you want to continue with this input? (yes/no): ").lower()

# Calculation
if ans == 'yes':
    d = f**2 - 4 * e * g  # Discriminant
    print("\nCalculating roots...")
    if d >= 0:
        root1 = (-f + (d ** 0.5)) / (2 * e)
        root2 = (-f - (d ** 0.5)) / (2 * e)
        print("\nThe roots of the equation are real and:")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    else:
        real_part = -f / (2 * e)
        imag_part = (abs(d) ** 0.5) / (2 * e)
        print("\nThe roots of the equation are complex and:")
        print(f"Root 1 = {real_part} + {imag_part}i")
        print(f"Root 2 = {real_part} - {imag_part}i")

    print('\n' + 'THANK YOU'.center(100))
    print('#' * 100)

elif ans == 'no':
    print('\n' + 'RESTART THE PROGRAM TO ENTER NEW VALUES.'.center(100))
    print('\n' + 'THANK YOU'.center(100))
    print('#' * 100)

else:
    print("\nInvalid input. Please restart the program and type 'yes' or 'no'.")
