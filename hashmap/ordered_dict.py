class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class OrderedDict:
    """
    A custom implementation of OrderedDict using a Hash Map and a Doubly Linked List.
    All operations (get, put, delete, move_to_end, popitem) should run in O(1) time.
    """

    def __init__(self):
        # Initialize sentinel dummy head and tail for the doubly linked list
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Map: key -> Node
        self.map = {}

    def __len__(self) -> int:
        return len(self.map)

    def __contains__(self, key) -> bool:
        return key in self.map

    def get(self, key, default=None):
        """Returns the value of the key if it exists, otherwise default."""
        # TODO: Implement this method
        return self.map[key].val if key in self.map else default

    def put(self, key, value) -> None:
        """
        Associates key with value. 
        If key already exists, updates the value and maintains its order.
        If key is new, inserts it at the end (before dummy tail).
        """
        # TODO: Implement this method
        if key in self.map:
            self.map[key].val = value # update value
        else:
            new_node = Node(key=key, val=value)
            prev_node = self.tail.prev # keep reference to current last node
            new_node.prev = prev_node # insert new last node
            new_node.next = self.tail # connect to tail
            prev_node.next = new_node # connect current last node to new last node
            self.tail.prev = new_node # connect tail to new last node
            self.map[key] = new_node # insert node to dict


    def delete(self, key) -> bool:
        """Removes the key from the dictionary. Returns True if removed, else False."""
        # TODO: Implement this method
        if key not in self.map:
            return False
        else:
            self.map[key].prev.next = self.map[key].next
            self.map[key].next.prev = self.map[key].prev
            del self.map[key]
            return True

    def move_to_end(self, key, last: bool = True) -> None:
        """
        Moves an existing key to either the end (last=True) or the beginning (last=False)
        of the doubly linked list. Raises KeyError if key does not exist.
        """
        # TODO: Implement this method
        pass

    def popitem(self, last: bool = True) -> tuple:
        """
        Removes and returns a (key, val) pair from the dictionary.
        If last=True, returns in LIFO order (from the end).
        If last=False, returns in FIFO order (from the beginning).
        Raises KeyError if the dictionary is empty.
        """
        # TODO: Implement this method
        pass

    def keys(self) -> list:
        """Returns a list of keys in the insertion order."""
        keys_list = []
        curr = self.head.next
        while curr != self.tail:
            keys_list.append(curr.key)
            curr = curr.next
        return keys_list


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Custom OrderedDict...")
    od = OrderedDict()
    
    # 1. Test basic puts and gets
    od.put("a", 1)
    od.put("b", 2)
    od.put("c", 3)
    
    assert od.get("a") == 1
    assert od.get("b") == 2
    assert od.get("c") == 3
    assert len(od) == 3
    assert od.keys() == ["a", "b", "c"]
    print("Basic insertion and order lookup passed!")

    # 2. Test update updates value but preserves original order
    od.put("b", 20)
    assert od.get("b") == 20
    assert od.keys() == ["a", "b", "c"]
    print("Update order preservation passed!")

    # 3. Test delete
    assert od.delete("b") is True
    assert od.get("b") is None
    assert od.keys() == ["a", "c"]
    assert len(od) == 2
    print("Deletion passed!")

    # 4. Test move_to_end (last=True)
    od.put("d", 4)  # order: a, c, d
    od.move_to_end("a", last=True)  # order: c, d, a
    assert od.keys() == ["c", "d", "a"]
    print("Move to end (last=True) passed!")

    # 5. Test move_to_end (last=False)
    od.move_to_end("d", last=False)  # order: d, c, a
    assert od.keys() == ["d", "c", "a"]
    print("Move to end (last=False) passed!")

    # 6. Test popitem LIFO
    k, v = od.popitem(last=True)  # removes "a", value 1
    assert k == "a" and v == 1
    assert od.keys() == ["d", "c"]
    print("Popitem LIFO passed!")

    # 7. Test popitem FIFO
    k, v = od.popitem(last=False)  # removes "d", value 4
    assert k == "d" and v == 4
    assert od.keys() == ["c"]
    print("Popitem FIFO passed!")
    
    print("All custom OrderedDict tests passed successfully!")
