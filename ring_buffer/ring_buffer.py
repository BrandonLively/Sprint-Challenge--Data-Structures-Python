from doubly_linked_list import DoublyLinkedList

#for commit
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.current = self.storage.add_to_tail(item)
        else:
            if self.current == self.storage.tail:
                self.storage.head.value = item
                self.current = self.storage.head
            else:
                self.current.next.value = item
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        for i in range(len(self.storage)):
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        # TODO: Your code here

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.pointer = 0

    def append(self, item):
        if self.pointer == len(self.storage):
            self.pointer = 0
        self.storage[self.pointer] = item
        self.pointer += 1

    def get(self):
        return [i for i in self.storage if i is not None]
