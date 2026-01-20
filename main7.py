def greet(name):
 print("Welcome to python function", name )

name = input("Enter your Name: ")
greet(name)

def check_abs(n):
    if n < 0:   # n = - 5
        return -n
    elif n >= 0 :  # n = 6
        return -n
    else:
        print("Invalid")


n=int(input("Enter your Number: "))
print("Absolute value of the number: " ,check_abs(n))


def palindrome (word):
    l = 0
    r = len(word) -1
    while l < r:
            if word[l] != word[r]:
                return False
            l = l+1
            r = r - 1
    return True
    

word= input("Enter any word: ")
if palindrome(word):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")