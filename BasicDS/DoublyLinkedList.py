class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode

    def deleteNode(self, data):
        if self.head is None:
            return

        currentNode = self.head
        if currentNode.data == data:
            self.head = currentNode.next
            if self.head:
                self.head.prev = None
            return

        while currentNode.next:
            if currentNode.next.data == data:
                currentNode.next = currentNode.next.next
                if currentNode.next:
                    currentNode.next.prev = currentNode
                return
            currentNode = currentNode.next

    def findNode(self, nodeData):
        currentNode = self.head

        while currentNode:
            if currentNode.data == nodeData:
                return currentNode
            currentNode = currentNode.next

    def displayList(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data, end=" <-> ")
            currentNode = currentNode.next
        print("None")

# Test Area
myList = DoublyLinkedList()
myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(3)
myList.deleteNode(2)
myList.displayList()
