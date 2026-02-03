mny_dict = {}
mhy_dict = {1:'apple', 2:'ball'}
my_dict = {'name':'Svanik', 'rollno':'6'}
mmy_dict={'name': 'John', 1: [2, 4, 3]}
new_dict={'name': 'John', 'age': '34', 1: [2, 4, 3]}
print(new_dict['name'])
print(new_dict.get('name'))

my_dict['rollno'] = 7
print(my_dict)

mhy_dict.pop(1)
print(mhy_dict)

mmy_dict.clear()
print(mmy_dict)

my_tuple = (1,2,3,4)
print(my_tuple)

my_t = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_t)
print(my_t[1])
print(my_t[2])
print(my_t[2][1])

jjk = ("p","e","r","m","i","t")
print("Sliced :", jjk[1:4])


print("Right angle traiangle star pattern")
n = int(input("Enter the row: "))
for i in range(1,n+1):
    for j in range(i):
        print(" * ", end="")
    print()