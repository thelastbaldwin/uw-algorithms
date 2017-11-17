class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class List():
    head = Node(None)

    def __init__(self, *initialValues):
        lastNode = None
        for i, value in enumerate(initialValues):
            if i == 0:
                self.head = Node(value)
                lastNode = self.head
            else: 
                newNode = Node(value)
                lastNode.next = newNode
                lastNode = newNode

    def __str__(self):
        listStr = ""
        currentNode = self.head;
        while currentNode is not None:
            separator = "->" if currentNode.next is not None else ""
            listStr = listStr + f"{currentNode}{separator}"
            currentNode = currentNode.next
        return listStr

    def reverse(self):
        prevNode = None
        node = self.head
        nextNode = None
    
        while node is not None:
          nextNode = node.next
          node.next = prevNode
          prevNode = node
          node = nextNode 
        
        self.head = prevNode
        return self

def Main():
    my_list = List(1, 2, 3, 4, 5)
    print(my_list)
    print(my_list.reverse())
Main()