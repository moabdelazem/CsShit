from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ANode = Node("A")
# BNode = Node("B")

# myQueue = deque()
# myQueue.append(ANode)
# myQueue.append(BNode)


class BT:
    def __init__(self):
        self.root = None

    # Insert Node
    def insertNode(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            return

        q = deque()
        q.append(self.root)
        while q:
            curr = q.popleft()
        
            if curr.left is None:
                curr.left = newNode
                break
            else:
                q.append(curr.left)
            
            if curr.right is None:
                curr.right = newNode
                break
            else:
                q.append(curr.right)
        
    # Traverse Display
    def dispBT(self):
        if self.root is None:
            return
        
        q = deque()
        q.append(self.root)

        while q:        
            curr = q.popleft()
            print(curr.data)

            if curr.left is not None:
                q.append(curr.left)
            elif curr.right is not None:
                q.append(curr.right)


myBT = BT()
myBT.insertNode(1)
myBT.insertNode(2)
myBT.insertNode(3)

