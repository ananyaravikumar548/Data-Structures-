class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node  # Points to itself
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_specific(self, data, value):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
            
        current = self.head
        while True:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break
        print(f"Value {value} not found - inserted at end")
        self.insert_at_end(data)

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
            
        if self.head.next == self.head:  # Single node
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
            return
            
        if self.head.next == self.head:  # Single node
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
            
        current = self.head
        prev = None
        while True:
            if current.data == value:
                if prev:  # Not head node
                    prev.next = current.next
                    if current == self.head:  # Update head if deleting head
                        self.head = current.next
                else:  # Head node
                    if current.next == self.head:  # Only one node
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = current.next
                        self.head = current.next
                return
                
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f"Value {value} not found")

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
            
        current = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Test the implementation
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_specific(25, 20)  # Insert 25 after 20
cll.traverse()

cll.delete_from_beginning()
cll.delete_from_end()
cll.traverse()

cll.delete_by_value(25)
cll.traverse()
