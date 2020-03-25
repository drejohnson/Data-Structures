from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {} # initialize storage
        self.amount = len(self.storage.keys()) # current number of nodes in cache
        self.linked_list = DoublyLinkedList() # set doubly linked list


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage.keys():
            return None
        else:
            self.linked_list.move_to_front(self.storage[key][1])
            return self.storage[key][0]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.linked_list.length == self.limit:
            old_key = self.linked_list.remove_from_tail()
            if key not in self.storage.keys():
                del self.storage[old_key] # deletes key 
            self.linked_list.add_to_head(key)
            self.storage[key] = (value, self.linked_list.head)
        else:
            self.linked_list.add_to_head(key)
            self.storage[key] =(value, self.linked_list.head)