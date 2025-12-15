import threading
from node import Node
from dll import DoublyLinkedList


class LRUCache:
    """Thread-safe LRU cache."""

    def __init__(self, capacity):
        self.capacity = capacity           # max items
        self.map = {}                      # key -> node
        self.dll = DoublyLinkedList()      # usage order
        self.lock = threading.Lock()       # single lock

    def get(self, key):
        """Return value or -1."""
        with self.lock:
            if key not in self.map:
                return -1
            node = self.map[key]
            self.dll.move_to_front(node)   # mark MRU
            return node.value

    def put(self, key, value):
        """Insert or update key."""
        with self.lock:
            if key in self.map:
                node = self.map[key]
                node.value = value
                self.dll.move_to_front(node)  # mark MRU
            else:
                if len(self.map) >= self.capacity:
                    tail = self.dll.remove_tail()  # evict LRU
                    if tail:
                        del self.map[tail.key]
                node = Node(key, value)
                self.dll.add_to_front(node)
                self.map[key] = node
