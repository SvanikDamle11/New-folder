x = int(input("Enter the 3 digit number :"))
z = x//10
#print("Q", z)
b = z//10               # % = R
print(b)                # // = Q
a = z%10
print(a)
y = x%10
print(y)
print(y*100+a*10+b*1)