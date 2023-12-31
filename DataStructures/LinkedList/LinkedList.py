class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
    
    def insert(self, newNode):
        self.tail.next = newNode
        self.tail = newNode
            
    def remove(self, data):
        current = self.head
        prev = None

        while current != None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    if current == self.tail:
                        self.tail = prev
                        prev.next = None
                    else:
                        prev.next = current.next
                break

            prev = current
            current = current.next

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)

    linkedList = LinkedList(node1)

    linkedList.insert(node2)
    linkedList.insert(node3)
    linkedList.insert(node4)

    print("\nBefore Removing...")
    linkedList.print()

    linkedList.remove(20)
    print("\nAfter Removing 20...")
    linkedList.print()

    linkedList.remove(40)
    print("\nAfter Removing 40...")
    linkedList.print()

    linkedList.insert(node5)
    print("\nAfter Inserting 50...")
    linkedList.print()