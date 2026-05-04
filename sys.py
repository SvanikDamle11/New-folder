#importing the module
import sys

def initial_phonebook():
    phone_book = []
    rows, cols = int(input("Enter the intials number of contacts: ")), 2
    print(phone_book)

    for i in range(rows):
        temp = []
        for j in range(cols):
            if j == 0:
               temp.append(str(input("Enter name*: ")))
            if j == 1:
               temp.append(int(input("Enter number*: ")))
        phone_book.append(temp)
    
    print(phone_book)
    return phone_book

def add_contact(pb):
   dip = []
   dip.append(str(input("Enter name: ")))
   dip.append(int(input("Enter number: ")))


   pb.append(dip)
   return pb

def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])


def remove_existing(pb):
    query = str(input("Please enter the name of the contact you wish to remove: "))
    temp =0
    for i in range(len(pb)):
        temp += 1
        print(pb.pop(i))
        print("This query has now been removed")
        return pb


def menu():
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