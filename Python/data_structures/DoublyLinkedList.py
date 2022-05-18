class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "{" \
               "value: " + str(self.value) + "}"
        # "next: " + str(self.next) + "}"


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        print(arr)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return None
        temp = self.tail.prev
        self.tail.prev = None
        self.tail = self.tail.prev
        temp.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            temp.prev = None
            self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length/2:
            temp_last = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_last = temp_last.prev
            return temp_last
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if self.length == 0:
            return False
        new_node = Node(value)
        prev_node = self.get(index)
        prev_node.value = new_node.value
        return True

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index)
            prev = temp.prev
            prev.next = new_node
            new_node.prev = prev
            new_node.next = temp
            temp.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        node = self.get(index)
        prev = node.prev
        after = node.next
        prev.next = after
        after.prev = prev
        node.next = None
        node.prev = None
        self.length -= 1
        return node


# Creating a new Double LL
dll = DoublyLinkedList(7)
# dll.print_list()

# append
dll.append(10)
dll.append(13)
dll.print_list()

# pop
# dll.pop()
# dll.print_list()
# dll.pop()
# dll.print_list()

# append
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.print_list()

# pop first
# dll.pop_first()
# dll.print_list()
# dll.pop_first()
# dll.print_list()

# prepend
# dll.prepend(6)
# dll.print_list()

# get by index
# print(dll.get(0))
# print(dll.get(1))
# print(dll.get(2))

# set
# dll.set_value(3, 25)
# dll.print_list()

# insert
# dll.insert(2, 24)
# dll.print_list()

# remove
# dll.remove(0)
# dll.print_list()