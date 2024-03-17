class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
    
    def printDetails(self):
        print(f"name: {self.name} \nroll: {self.roll}")


s1 = Student("23951A055F", "Mohammed Safwan")
s1.printDetails()