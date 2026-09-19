x = range(5)
print(list(x))

print(list(range(7)))

print(list(range(1,10)))

print(list(range(0,25,5)))

print(list(range(2,11,2)))

print(list(range(1,11,2)))

print(list(range(10,0,-1)))

print(list(range(50,0,-2)))

for i in range (5):
 print(i)

 for i in range(1,11):
  print(i)

for i in range(1,11):
 print(5*i) 

total = 0
for i in range (1,11):
 total=total+i

print(total)

for i in range (555):
 print("Prashanth")

x = eval("10+50")
print(x)


a = 10
b = 5
result = eval("a+b")

print(result)


x = input("enter expression:")
print(eval(x))


print(eval("10>5"))

print(eval("10>5 and 20>10"))

x=eval("10.5")
print(x)
print(type(x))


name = "Prashanth"
age = 18
print(f"my name is {name}an i am {age} years old.")


name = "prash"
calss = "btec"
print(f"my name is {name}and i am {calss} student")


name = "Prashanth"
age = 18
city = "mysore"
print(f"myself {name},and i am {age} years old,and i  live in {city}")




a = 10
b = 20
print(f"the sum is {a+b}")



price = 800
quantity = 8
print(f"total price of the product is {price*quantity}")


name = "prash"
age = 18
print("i am {0} and my age is {1}.".format(name,age))


price = 99.99999
print(f"Price:{price:.2f}")


num = 12.55847954461348461146
print(f"{num:.2f}")



price = 1054879632587463
print(f"{price:,}")

percentage = 0.856
print(f"{percentage:.2%}")

print(f"10+20 = {10+20}")

x = 5
print(f"{x} squared is {x**2}")

name = input("enter the name :")
age = int(input("enter the age :"))

print(f"Hello {name}, are you{age} year old")

name = "prasha"
age = 18
print("myself %s and i am %d years old."%(name,age))


name = "prashanth" 
calss = 10
college = "BIT"
print(f"myself {name}, and i am student of class {calss} in {college}.")


for i in range (10):
 print("Prashanth")


 i = 1
 while i<=5:
    print(i)
    i = i+1

for i in range(1,10):
 if i ==6:
  break
 print(i)


 for i in range(1,10):
  if i ==3:
   continue
  print(i)