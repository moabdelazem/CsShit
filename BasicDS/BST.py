class Node:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

# Node & Parent Class
class NodeAndParent:
    def __init__(self, node=None, parent=None, isLeft=None):
        self.node = node
        self.parent = parent
        self.isLeft = isLeft

# Binary Search Tree Structure 
class BinarySearchTree:
    def __init__(self):
        self.rootNode = None
    
    # Insert Node In Binary Tree {Iterative Approach}
    def insertNode(self, data):
        newNode = Node(data)

        if self.rootNode is None:
            self.rootNode = newNode
            return 
        
        currentNode = self.rootNode
        while currentNode:
            if currentNode.data < data:
                if currentNode.leftNode is None:
                    currentNode.leftNode = newNode
                    break
                else:
                    currentNode = currentNode.leftNode
            else:
                if currentNode.rightNode is None:
                    currentNode.rightNode = newNode
                    break
                else:
                    currentNode = currentNode.rightNode
            
    # Find Specific Node {Iterative Approach}
    def findNode(self, nodeData):
        currentNode = self.rootNode

        while currentNode:
            if currentNode.data == nodeData:
                return currentNode
            elif currentNode.data > nodeData:
                currentNode = currentNode.leftNode
            else:
                currentNode = currentNode.rightNode
        return None

    # Find Node And Parent
    def findNodeAndParent(self, nodeData):
        currentNode = self.rootNode
        parentNode = None
        isLeft = None
        nodeAndParentInfo = None

        while currentNode:
            if currentNode.data == nodeData:
                nodeAndParentInfo = NodeAndParent(currentNode, parentNode, isLeft)
                break
            elif currentNode.data > nodeData:
                parentNode = currentNode
                isLeft = True
                currentNode = currentNode.leftNode
            else:
                parentNode = currentNode
                isLeft = False
                currentNode = currentNode.rightNode
        return nodeAndParentInfo

    # Order Traversals
    """ 
        PreOrder    =>> Node -> Left -> Right
        InOrder     =>> Left -> Node -> Right
        PostOrder   =>> Left -> Right -> Node
    """
    def InOrder(self):
        self.internalInOrder(self.rootNode)

    def internalInOrder(self, node):
        if node is not None:            
            self.internalInOrder(node.leftNode)
            print(node.data, " -> ", end=' ')
            self.internalInOrder(node.rightNode)

    