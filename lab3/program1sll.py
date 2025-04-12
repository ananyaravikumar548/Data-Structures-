class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
    
    def insert_specific(self, data, value):
        new_node = Node(data)
        current = self.head
        while current is not None and current.data != value:
            current = current.next
            new_node.next = current.next
            current.next = new_node
        
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
            current.next = current.next.next

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Singly Linked List Elements:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
        
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_specific(25,20)  # Insert 20 after 15
sll.traverse()


sll.delete_from_beginning()
sll.delete_from_end()
sll.traverse()
sll.delete_by_value(20)
sll.traverse()

