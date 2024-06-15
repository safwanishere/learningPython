class A:
    def method1(self):
        print("hello")

    def method1(self, name):
        print(f"hello {name}")

    def method1(self, name, age):
        print(f"hello {name} - {age} years old")

person = A()
person.method1("yahya", 27)

# same method name, same class, different method signature
# the latest declaration of method with the same name is considered