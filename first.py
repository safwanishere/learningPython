#----------------------------------

# sum of the digits of an integer

a = int(input())
sum = 0
while a>0:
    dig = a%10
    sum += dig
    a = int(a/10)
print("sum:", sum)

#-----------------------------------

# revere an integer

b = int(input())
rev = 0
while b>0:
    dig = b%10
    rev = rev*10 + dig
    b = int(b/10)
print("reverse:", rev)

#-----------------------------------

# swapping two integers

a,b = input().split()
a,b = b,a
print("a:", a)
print("b:", b)

#-----------------------------------

# sum of two numbers

a,b = input().split()
print("sum:", a+b)

#-----------------------------------

# difference of two numbers

a,b = input().split()
print("difference:", a-b)

#-----------------------------------

# product of two numbers

a,b = input().split()
print("product:", a*b)

#-----------------------------------

# quotient of two numbers

a,b = input().split()
print("quotient:", a/b)

#-----------------------------------

# sum of three numbers

a,b,c = input().split()
print("sum:", a+b+c)

#-----------------------------------

# product of three numbers

a,b,c = input().split()
print("product:", a*b*c)

#-----------------------------------

# printing multiplication table

a = int(input)
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")

#-----------------------------------