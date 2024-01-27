class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack Class Structure
class Stack:
    def __init__(self):
        self.top = None
    
    # Push
    def push(self, data):
        newNode = Node(data)

        newNode.next = self.top
        self.top = newNode
    
    # Pop
    def pop(self):
        self.top = self.top.next
    
    # Peek
    def peek(self):
        return self.top.data

    # Display
    def display_stack(self):
        curr = self.top
        while curr:
            print(curr.data, end="\n")
            curr = curr.next
    
