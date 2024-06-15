class A:
    def method1(self):
        print("hello from A")

class B(A):
    def method1(self):
        print("hello from B")

objectA = A()
objectB = B()
objectA.method1()
objectB.method1()

# same method name, same method signature, different class
# considers the method defined in the class of the object