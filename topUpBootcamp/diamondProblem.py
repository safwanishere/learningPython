class A:
    def method_a(Self):
        print("in method a")
    def common_method(self):
        print("im in class A")

class B:
    def method_b(self):
        print("in method b")
    def common_method(self):
        print("im in class B")
    
class Driver(B, A):
    pass

ob = Driver()
ob.method_a()
ob.method_b()
ob.common_method()