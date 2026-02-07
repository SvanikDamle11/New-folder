x = int(input("Enter a 3 digit number :"))
z = 10
a = x%z
print(a)
b = x//z
#print(b)
c = b%z
print(c)
d = b//z
print(d)
ans = d+c*c+a*a*a
print(ans)
if ans == x:
    print("it is a disarium number")
else:
    print("it is not a disarium number")


