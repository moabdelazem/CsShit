# Node Class Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Structure
class LinkedList:
    def __init__(self):
        self.headNode = None
    
    # Add Node At The First Of The List
    def insertNode(self, data):
        newNode = Node(data)

        newNode.next = self.headNode
        self.headNode = newNode

    # Add Node At The End Of The List
    def insertLast(self, data):
        currentNode = self.headNode
    

        if currentNode is not None:
            newNode = Node(data)

            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
        else:
            self.insertNode(data)                

    
    # Add Node After Other Selected Node
    def insertAfter(self, nodeData, data):
        currentNode = self.findNode(nodeData)

        if currentNode is not None:
            newNode = Node(data)

            newNode.next = currentNode.next
            currentNode.next = newNode
        else:
            return None
    
    # Add Node Before Other Selected Node
    def insertBefore(self, nodeData, data) -> None:
        currentNode = self.findNode(nodeData)
        prevNode = self.findParent(nodeData)

        newNode = Node(data)

        if prevNode is None:
            self.insertNode(data)
        else:
            newNode.next = currentNode
            prevNode.next = newNode
    
    # Delete Node
    def deleteNode(self, nodeData) -> None:
        currentNode = self.findNode(nodeData)
        prevNode = self.findParent(nodeData)

        if currentNode is not None:
            if prevNode is None:
                self.headNode = self.headNode.next
            elif currentNode.next is None:
                prevNode.next = None
            else:
                prevNode.next = currentNode.next


    # Find Specfic Node By Data
    def findNode(self, nodeData) -> Node:
        currentNode = self.headNode

        while currentNode:
            if currentNode.data == nodeData:
                return currentNode
            currentNode = currentNode.next
        return None
    
    # Find Parent Of Node By Data
    def findParent(self, nodeData) -> Node:
        currentNode = self.headNode

        while currentNode.next:
            if currentNode.next.data == nodeData:
                return currentNode
            currentNode = currentNode.next
        return None

    # Count The Elements
    def countListNodes(self):
        currentNode = self.headNode
        counter = 0

        while currentNode:
            counter += 1
            currentNode = currentNode.next
        return counter

    # Display List
    def dispList(self):
        currentNode = self.headNode

        while currentNode:
            print(currentNode.data, end=" => ")
            currentNode = currentNode.next
        print("None\n")

    # Reverse LinkedList
    # Iterative Approach
    def reverseList(self):
        prevNode, currentNode = None, self.headNode
        # O(n)
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.headNode = prevNode

    # Remove Dups From List
    def removeDups(self):
        if self.headNode is None:
            return self.headNode
        
        # My Set 
        mySet = set()

        currentNode = self.headNode
        mySet.add(self.headNode.data)

        while currentNode.next:
            if currentNode.next.data in mySet:
                currentNode.next = currentNode.next.next
            else:
                mySet.add(currentNode.data)
                currentNode = currentNode.next
        
        return self.headNode