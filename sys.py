#importing the module
import sys

def initial_phonebook():
    phone_book = []
    rows, cols = int(input("Enter the intials number of contacts: ")), 2
    print(phone_book)

for i in range(rows):
    
    print("You can perform the following operations on the phonebook \n")
    print("1. Add a new contact")
    print("2. Display all contacts")
    print("3. Remove an existing contact")
    print("4. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice


ch = 1
pb = initial_phonebook
while ch in (1,2,3,4):
    ch = menu()
    if ch == 1:
     pb = add_contact(pb)

    elif ch == 2:
     display_all(pb)
    
    elif ch == 3:
     remove_existing(pb)

    elif ch == 4:
      print("Thank you for using Phonebook")    
      sys.exit("Goodbye have a nice day ahead")