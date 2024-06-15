from abc import ABC, abstractmethod

class Sample(ABC):
    @abstractmethod
    def hello(self):
        pass

    def sayHi(self):
        print("Hi!")
    
class Example(Sample):
    def hello(self):
        print("say hello")

ob = Example()
ob.hello()