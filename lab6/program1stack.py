class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None  # or print("Stack is underflow")
        else:
            popped_data = self.top
            self.top = self.top.next
            return popped_data.data

    def peek(self):
        if self.top is None:
            return None  # or print('stack is empty')
        else:
            return self.top.data

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

# Test code
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # Output: 30
print(s.pop())  # Output: 20
print(s.pop())  # Output: 10
print(s.is_empty())  # Output: True
