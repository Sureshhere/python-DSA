#implementing stacks using single linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.num_elements == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)


print(stack.peek())  # prints 3
print(stack.pop())   # prints 3
print(stack.pop())   # prints 2
print(stack.is_empty())  # prints False
print(stack.pop())   # prints 1
print(stack.is_empty())  # prints True
