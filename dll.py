from node import Node


class DoublyLinkedList:
    """DLL with sentinels."""

    def __init__(self):
        self.head = Node(None, None)  # dummy head
        self.tail = Node(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        """Insert after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        """Detach node."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_front(self, node):
        """Mark as MRU."""
        self.remove(node)
        self.add_to_front(node)

    def remove_tail(self):
        """Pop LRU node."""
        node = self.tail.prev
        if node == self.head:
            return None  # empty list
        self.remove(node)
        return node
