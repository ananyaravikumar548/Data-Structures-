class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_specific(self, data, value):
        new_node = Node(data)
        current = self.head

        if current is None:
            self.head = new_node
            return
    
        while current is not None:
            if current.data == value:
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        
        print(f"Value {value} not found - inserted at end")
        self.insert_at_end(data)

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None

    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
    
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev:  # Not the head node
                    current.prev.next = current.next
                else:  # Deleting head node
                    self.head = current.next
                
                if current.next:  # Not the tail node
                    current.next.prev = current.prev
                return
            current = current.next
        
        print(f"Value {value} not found")

    def traverse_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Doubly Linked List Elements:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def traverse_backward(self):
        if self.head is None:
            print("List is empty.")
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
            
        print("Doubly Linked List (Reverse):", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Test the implementation
dll = DoublyLinkedList()
dll.insert_at_end(50)
dll.insert_at_end(5)
dll.insert_at_end(10)
dll.insert_at_end(15)
dll.insert_specific(20, 15)
dll.traverse_forward()

dll.delete_from_beginning()
dll.delete_from_end()
dll.traverse_forward()

dll.delete_by_value(10)
dll.traverse_forward()

dll.traverse_backward()
