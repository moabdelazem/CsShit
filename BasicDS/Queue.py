class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert At Last (EnQueue)
    def enQueue(self, data):
        newNode = Node(data)

        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    # Remove Node From The First Of The Queue
    def deQueue(self):
        delNode = self.front
        self.front = self.front.next

        return delNode

    def dispQueue(self):
        curr = self.front

        while curr:
            print(curr.data, " => ") 
            curr = curr.next
        
           

