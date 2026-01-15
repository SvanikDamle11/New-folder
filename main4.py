x = int(input("Enter the number :"))
for i in range(1,11):
   print(x,"*",i,"=",x*i) 



n = int(input("Enter the Number of terms: "))
num = 1
sum = 0
while(num <= n):
 sum = sum +num
 num = num+ 1


print("The sum is: ", sum)


print("Program to check whether the number is prime Number or not")
u = int(input("Enter the Number: "))
if u <= 1:
    print("Not a prime Number")
else:
    for i in range(2,u):
        if u % i == 0:
            print(" Not a Prime Number")
            break
              
    else:
        print(" Prime Number")