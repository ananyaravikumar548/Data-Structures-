class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None  # Fixed variable names

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f'Enqueued item is {self.rear.data}')

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return None
            
        temp = self.front
        self.front = temp.next
        deleted_item = temp.data
        
        if self.front is None:
            self.rear = None  # Reset rear when queue becomes empty
            
        print(f"Dequeued item from the Queue is {deleted_item}")
        return deleted_item

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return
            
        current = self.front
        print("Queue elements: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()    # Show queue elements: 10 -> 20 -> 30 -> None
    q.dequeue()    # Remove front element (10)
    q.display()    # Display after dequeue: 20 -> 30 -> None
