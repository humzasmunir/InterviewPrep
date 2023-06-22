class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
    
    def insert(self, newNode):
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, data):
        current = self.head
        prev = None

        while current != None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    current.next.prev = None
                else:
                    if current == self.tail:
                        self.tail = prev
                        prev.next = None
                    else:
                        prev.next = current.next
                        current.next.prev = prev
                break

            prev = current
            current = current.next

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    
    def printBackwards(self):
        current = self.tail
        while current != None:
            print(current.data)
            current = current.prev

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)

    doublyLinkedList = DoublyLinkedList(node1)

    doublyLinkedList.insert(node2)
    doublyLinkedList.insert(node3)
    doublyLinkedList.insert(node4)

    print("\nBefore Removing...")
    print("Forwards:")
    doublyLinkedList.print()
    print("Backwards:")
    doublyLinkedList.printBackwards()

    doublyLinkedList.remove(20)
    print("\nAfter Removing 20...")
    print("Forwards:")
    doublyLinkedList.print()
    print("Backwards:")
    doublyLinkedList.printBackwards()

    doublyLinkedList.remove(40)
    print("\nAfter Removing 40...")
    print("Forwards:")
    doublyLinkedList.print()
    print("Backwards:")
    doublyLinkedList.printBackwards()

    doublyLinkedList.insert(node5)
    print("\nAfter Inserting 50...")
    print("Forwards:")
    doublyLinkedList.print()
    print("Backwards:")
    doublyLinkedList.printBackwards()