from LinkedList import LinkedList

myBasicList = LinkedList()

myBasicList.insertNode(1)
myBasicList.insertNode(2)
myBasicList.insertNode(3)

# Insert last
myBasicList.insertLast(4)

# Insert after
myBasicList.insertAfter(2, 5)

# Insert before
myBasicList.insertBefore(4, 6)

# Delete node
myBasicList.deleteNode(2)

# Display list
myBasicList.dispList()

# Insert Dups
myBasicList.insertNode(2)
myBasicList.insertNode(3)
myBasicList.insertNode(4)

# # Remove duplicates
# myBasicList.removeDups()

myBasicList.dispList()

myBasicList.reverseList()

myBasicList.removeDups()

myBasicList.dispList()