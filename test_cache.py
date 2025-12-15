import threading
from cache import LRUCache


def test_eviction():
    """Evict LRU on exceed."""
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # make 2 LRU
    cache.put(3, 3)    # evicts 2
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3
    print("✓ test_eviction passed")


def test_update():
    """Update keeps key."""
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10
    print("✓ test_update passed")


def test_capacity_one():
    """Capacity = 1 behavior."""
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    print("✓ test_capacity_one passed")


def test_access_order():
    """Access updates order."""
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)
    cache.get(2)
    cache.put(4, 4)
    assert cache.get(3) == -1
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(4) == 4
    print("✓ test_access_order passed")


def test_thread_safety():
    """Concurrent access OK."""
    cache = LRUCache(100)
    errors = []

    def writer(start):
        try:
            for i in range(start, start + 50):
                cache.put(i, i * 10)
        except Exception as e:
            errors.append(e)

    def reader(start):
        try:
            for i in range(start, start + 50):
                cache.get(i)
        except Exception as e:
            errors.append(e)

    threads = []
    for i in range(5):
        t1 = threading.Thread(target=writer, args=(i * 50,))
        t2 = threading.Thread(target=reader, args=(i * 50,))
        threads.extend([t1, t2])

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(errors) == 0
    print("✓ test_thread_safety passed")


def test_get_nonexistent():
    """Missing key returns -1."""
    cache = LRUCache(2)
    assert cache.get(999) == -1
    print("✓ test_get_nonexistent passed")


if __name__ == "__main__":
    test_eviction()
    test_update()
    test_capacity_one()
    test_access_order()
    test_thread_safety()
    test_get_nonexistent()
    print("\nAll tests passed")
