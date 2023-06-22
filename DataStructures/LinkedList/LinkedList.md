# LinkedList

LinkedList is a Python implementation of a singly linked list data structure. A linked list is a linear data structure consisting of nodes, where each node contains a value and a reference (or link) to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for efficient insertions and removals at the cost of slower access to elements.

## Features

- Insert nodes at the end of the linked list.
- Remove nodes from the linked list by value.
- Print the elements of the linked list.

## Runtime Complexity

The runtime complexity of various operations on a linked list is as follows:

- Insertion at the end: O(1)
- Removal by value: O(n) (worst case, when the value is in the last node or not present)
- Printing the elements: O(n)

## Usage

To use the LinkedList class, follow these steps:

1. Import the LinkedList and Node classes:

   ```python
   from linkedlist import LinkedList, Node
   ```

2. Create nodes with the desired data:

   ```python
   node1 = Node(10)
   node2 = Node(20)
   ```

3. Create a linked list and initialize it with a node:

   ```python
   linked_list = LinkedList(node1)
   ```

4. Insert nodes at the end of the linked list:

   ```python
   linked_list.insert(node2)
   ```

5. Remove nodes from the linked list by value:

   ```python
   linked_list.remove(20)
   ```

6. Print the elements of the linked list:

   ```python
   linked_list.print_list()
   ```

## Example

Here's an example of how to use the LinkedList class:

```python
from linkedlist import LinkedList, Node

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Create a linked list and insert nodes
linked_list = LinkedList(node1)
linked_list.insert(node2)
linked_list.insert(node3)

# Print the elements of the linked list
linked_list.print_list()

# Output:
# 10
# 20
# 30
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

This LinkedList implementation is inspired by the concepts taught in computer science courses and various programming resources.
