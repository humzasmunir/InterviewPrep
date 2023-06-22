# Doubly Linked List

Doubly Linked List is a Python implementation of a doubly linked list data structure. A doubly linked list is similar to a singly linked list, but each node has an additional pointer that points to the previous node in the sequence. This allows for efficient traversal both forward and backward in the list.

## Features

- Insert nodes at the end of the doubly linked list.
- Remove nodes from the doubly linked list by value.
- Print the elements of the doubly linked list both forwards and backwards.

## Usage

To use the DoublyLinkedList class, follow these steps:

1. Import the `DoublyLinkedList` and `Node` classes:

   ```python
   from doublylinkedlist import DoublyLinkedList, Node
   ```

2. Create nodes with the desired data:

   ```python
   node1 = Node(10)
   node2 = Node(20)
   ```

3. Create a doubly linked list and initialize it with a node:

   ```python
   doublyLinkedList = DoublyLinkedList(node1)
   ```

4. Insert nodes at the end of the doubly linked list:

   ```python
   doublyLinkedList.insert(node2)
   ```

5. Remove nodes from the doubly linked list by value:

   ```python
   doublyLinkedList.remove(20)
   ```

6. Print the elements of the doubly linked list:

   ```python
   print("Forwards:")
   doublyLinkedList.print()
   
   print("Backwards:")
   doublyLinkedList.printBackwards()
   ```

## Example

Here's an example of how to use the DoublyLinkedList class:

```python
from doublylinkedlist import DoublyLinkedList, Node

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Create a doubly linked list and insert nodes
doublyLinkedList = DoublyLinkedList(node1)
doublyLinkedList.insert(node2)
doublyLinkedList.insert(node3)
doublyLinkedList.insert(node4)

# Print the elements of the doubly linked list
print("\nBefore Removing...")
print("Forwards:")
doublyLinkedList.print()
print("Backwards:")
doublyLinkedList.printBackwards()

# Remove a node from the doubly linked list
doublyLinkedList.remove(20)
print("\nAfter Removing 20...")
print("Forwards:")
doublyLinkedList.print()
print("Backwards:")
doublyLinkedList.printBackwards()

# Remove another node from the doubly linked list
doublyLinkedList.remove(40)
print("\nAfter Removing 40...")
print("Forwards:")
doublyLinkedList.print()
print("Backwards:")
doublyLinkedList.printBackwards()

# Insert a new node at the end of the doubly linked list
doublyLinkedList.insert(node5)
print("\nAfter Inserting 50...")
print("Forwards:")
doublyLinkedList.print()
print("Backwards:")
doublyLinkedList.printBackwards()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

This Doubly Linked List implementation is inspired by the concepts taught in computer science courses and various programming resources.