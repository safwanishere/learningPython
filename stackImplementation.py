class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("stack is empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("stack is empty")

    def size(self):
        return len(self.items)   
    
stack = Stack()
stack.push(5)
stack.push(7)
stack.push(3)
print(stack.peek())
stack.pop()
stack.push(1)
stack.push(9)
print(stack.peek())