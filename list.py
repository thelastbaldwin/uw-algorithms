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

    def get_index(self, index):
        current_node = self.head
        while index > 0:
            current_node = current_node.next
            index -= 1
        return current_node

    def count_iterative(self):
        i = 1
        current = self.head
        while current.next is not None:
            current = current.next
            i += 1
        return i

def Main():
    my_list = List(1, 2, 3, 4)
    print(my_list);
Main()