# TreeNode Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree Structure
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Insert Node Iterative Approach
    def insertNode(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            return

        currentNode = self.root
        while currentNode:
            if data > currentNode.data:
                if currentNode.left is None:
                    currentNode.left = newNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    break
                else:
                    currentNode = currentNode.right

    # Find Node Iterative Approach
    def findNode(self, nodeData):
        currentNode = self.root

        while currentNode:
            if nodeData == currentNode.data:
                return currentNode
            elif nodeData < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None 

    # Display Binary Search Tree (In-order Traversal) {Left -> Node -> Right}
    def IndisplayTree(self, node):
        if node is not None:
            self.IndisplayTree(node.left)
            print(node.data, end=" ")
            self.IndisplayTree(node.right)

    # Display Binary Search Tree (Pre-Order Traversal) (Node -> Left -> Right)
    def PredisplayTree(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.PredisplayTree(node.left)
            self.PredisplayTree(node.right)

    # Display Binary Search Tree (Post-Order Traversal) (Left -> Right -> Node)
    def PostdisplayTree(self, node):
        if node is not None:
            self.PostdisplayTree(node.left)
            self.PostdisplayTree(node.right)
            print(node.data, end=" ")

fuckingTree = BinarySearchTree()
fuckingTree.insertNode(1)
fuckingTree.insertNode(2)
fuckingTree.insertNode(3)
fuckingTree.insertNode(4)
fuckingTree.insertNode(5)
fuckingTree.insertNode(6)
fuckingTree.insertNode(7)
fuckingTree.insertNode(8)
fuckingTree.insertNode(9)

# print(fuckingTree.root.data)
fuckingTree.IndisplayTree(fuckingTree.root)
fuckingTree.PredisplayTree(fuckingTree.root)
fuckingTree.PostdisplayTree(fuckingTree.root)


