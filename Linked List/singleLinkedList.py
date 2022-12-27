class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data, prev_node.next)
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_node_at_pos(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            return
        prev = None
        count = 0
        while current and count != pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return
        prev.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        if current is None:
            print('Null')


# Create a single linked list
linked_list = LinkedList()

# Add nodes to the single linked list
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)

#print the single linked list
linked_list.print_list()

#delete node with data 3
linked_list.delete_node(3)

linked_list.print_list()


