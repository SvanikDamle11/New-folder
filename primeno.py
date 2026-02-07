x = int(input("Enter the number :"))
if x <= 1:
    print("Not a prime number")
else:
    for i in range(2,x):
        if x % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")    


