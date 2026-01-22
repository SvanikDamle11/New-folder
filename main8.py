class Parrot:
    # Class attribute
    species = "Bird"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    def sing(self, song):
        # Using self.name to personalize the output
        print(f"{self.name} is singing: {song}")

# Creating the object
obj = Parrot("SvanikDamle7", 12)

# Calling the method
obj.sing("Happy Happy")



class Student:
    def __init__(self, name, rollno):
        # Instance attributes
        self.name = name
        self.rollno = rollno

    def info(self):
        # Using self.name to personalize the output
            print(f"{self.name} is of rollno. {self.rollno}")

        
obj1 = Student("SvanikDamle7", 7)
obj1.info()