# first inital code for leapfrog day 1 
print("hello world!!")


#input test
x = int(input("Enter the value for x(even or odd): "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")


#prime number test
num = int(input("Enter a number(prime or not): "))

if num <= 1:
    print(" not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime number")
    else:
        print(" not a prime number")
