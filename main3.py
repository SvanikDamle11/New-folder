lst = ['Pizza','Fries','Fried Chicken','Chicken Nuggets','Mirinda']
print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])
lst.append('Chilli Chicken')
print("Updated List :", lst)
lst.remove('Mirinda')
print("Updated List :", lst)
lst.sort()
print("Sorted List:", lst)
lst.reverse()
print("Reversed List:", lst)
lst =lst[1:4]
print("Sliced List", lst)
lst.clear()
print("Cleared list")


n = int(input("Enter the number:"))
if n > 0:
 print("Positive Number")
elif n < 0 :
 print("Negative number")
else:
 print("Neutral")


x = int(input("Enter the number:"))
if x % 2 == 0:
 print("Even Number")
else:
 print("Odd Number")


 