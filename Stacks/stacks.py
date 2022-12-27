# Stack class
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# Testing the stack
s = Stack()
print(s.is_empty()) # True

s.push(1)
s.push(2)
s.push(3)
print(s.peek()) # 3
print(s.size()) # 3
print(s.is_empty()) # False

s.pop()
print(s.peek()) # 2
print(s.size()) # 2
