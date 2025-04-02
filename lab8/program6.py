class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,data):
        newnode= Node(data)
        if self.rear is None:
            self.rear=self.front=newnode
            return
    
        else:
            self.rear.next=newnode
            self.rear=newnode
        print(f"enqueue:{self.rear.data}")
    
    def dequeue(self):
        if self.front is None:
            print("empty")
        else:
            temp =self.front
            self.front=temp.next
            deleted=temp.data
            del(temp)
            temp=None
            print(deleted)
        
        
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
