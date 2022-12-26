class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data, None, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_before(self, ref_node, data):
        if ref_node is None:
            print("Reference node is not in the list")
            return
        new_node = Node(data, None, None)
        new_node.prev = ref_node.prev
        new_node.next = ref_node
        if ref_node.prev is None:
            self.head = new_node
        else:
            ref_node.prev.next = new_node
        ref_node.prev = new_node

    def insert_after(self, ref_node, data):
        if ref_node is None:
            print("Reference node is not in the list")
            return
        new_node = Node(data, None, None)
        new_node.prev = ref_node
        new_node.next = ref_node.next
        if ref_node.next is None:
            self.tail = new_node
        else:
            ref_node.next.prev = new_node
        ref_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "->", end=" ")
            current_node = current_node.next
        if current_node is None:
            print('Null')


# create a new empty list
dl_list = DoublyLinkedList()

# append some data to the list
dl_list.append(1)
dl_list.append(2)
dl_list.append(3)

# prepend some data to the list
dl_list.prepend(0)

# insert a new node before the node with data 1
dl_list.insert_before(dl_list.head.next, 10)

# insert a new node after the node with data 1
dl_list.insert_after(dl_list.head.next, 50)

# print list
dl_list.print_list()


