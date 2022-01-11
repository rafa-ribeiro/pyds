class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Value: {self.value} | Next: {self.next.value}"


class LinkedList:

    def __init__(self):
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None
        self._size = 0

    def append(self, value):
        item_node = LinkedListNode(value=value)
        if self.head is None:
            self.head = self.tail = item_node
        else:
            self.tail.next = item_node
            self.tail = item_node

        self._size += 1

    def delete(self, value):
        if not self.head:
            return

        # if value to remove is in head, remove it and set new head
        if value == self.head.value:
            self.delete_head()
            return

        # if the value is not in the head, look for it in the rest of the list
        self._delete_value(value=value)

    def delete_head(self):
        self.head = self.head.next
        self._size -= 1

        if len(self) == 0:
            self.head = None
        elif len(self) == 1:
            self.tail = None

    def delete_tail(self):
        self._delete_value(self.tail.value)

    def _delete_value(self, value):
        before_node = self.head
        curr_node = self.head.next
        found = False
        idx = 1
        while curr_node and not found:
            if curr_node.value == value:
                found = True
            else:
                before_node = curr_node
                curr_node = curr_node.next
                idx += 1

        if found:
            before_node.next = curr_node.next
            self._size -= 1
            # if the list has a size equal to 1, there is no tail value
            if len(self) == 1:
                self.tail = None
            # if value is in tail, remove it and set new tail
            elif idx == self._size:
                self.tail = before_node

    def __len__(self):
        return self._size

    def __iter__(self):
        self.idx = 0
        self.iter_list = []

        if self.head:
            _values = [self.head.value]
            curr_node = self.head.next
            while curr_node:
                _values.append(curr_node.value)
                curr_node = curr_node.next

            self.iter_list = _values
        return self

    def __next__(self):
        if self.idx < self._size:
            _next = self.iter_list[self.idx]
            self.idx += 1
            return _next
        else:
            raise StopIteration
