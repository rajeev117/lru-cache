# Thread-Safe LRU Cache (Python)

## Problem Statement
Design and implement a Least Recently Used (LRU) cache with fixed capacity
supporting O(1) get and put operations.

## Design
HashMap for O(1) key lookup
Doubly Linked List to maintain usage order
Most recently used item at the head
Least recently used item at the tail

## Thread Safety
A single lock is used to ensure correctness under concurrent access.

## Time Complexity
get: O(1)
put: O(1)

## Space Complexity
O(capacity)

## Limitations
Single lock limits parallel reads
In-memory only

## Possible Improvements
Read-write locks
TTL-based eviction
Sharding for scalability
