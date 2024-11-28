class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, data):
        self.stack.append(data)

    def remove(self):
        self.stack.pop()

    def print(self):
        print(self.stack)

    def getTopItem(self):
        return self.stack[-1]

test = Stack()
test.add("hello world")
test.add("|Another item in the stack.")
test.print()

test.remove()

print(test.getTopItem())