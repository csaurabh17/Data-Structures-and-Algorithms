class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        if other.value == self.value and other.next == self.next:
            return True
        else:
            return False

    def __str__(self):
        return "{" \
               "value: " + str(self.value) + "}"
        # "next: " + str(self.next) + "}"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        prev_node = self.traverse()
        self.tail = prev_node
        prev_node.next = None
        self.length -= 1
        return self

    def traverse(self):
        temp = self.head
        while temp is not None:
            if temp.next == self.tail:
                return temp
            else:
                temp = temp.next

    def print_list(self):
        temp = self.head
        lst = []
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        print(lst)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def pop_first(self):
        print(self.length)
        if self.length == 0:
            print('No items to pop first')
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.length -= 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            prev = self.head
            for i in range(index):
                if i == index:
                    prev = temp
                temp = temp.next
            new_node.next = prev.next
            prev.next = new_node
            self.length -= 1
        return self

    def remove(self, index):
        if self.length == 0:
            return None
        elif index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            new_pointer = temp.next
            prev.next = new_pointer
            temp.next = None
            return temp.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


new_ll = LinkedList(4)

# testing append
new_ll.append(3)
new_ll.append(2)
# print(new_ll.tail.value)

# printing post append
# new_ll.print_list()

# popping element
# print(new_ll.pop())
# print(new_ll.pop())
# print(new_ll.pop())
# new_ll.print_list()

# testing prepend
# new_ll.prepend(1)
# new_ll.prepend(2)
# new_ll.print_list()


# popping the first item
# print('before popping first')
# new_ll.print_list()
# new_ll.pop_first()
# print('after popping first element')
# new_ll.print_list()
# new_ll.pop_first()
# print('after popping first element')
# new_ll.print_list()
# print('before popping first')
# new_ll.pop_first()
# new_ll.print_list()
# print('before popping first')
# new_ll.pop_first()
# new_ll.print_list()

# get by index
# print(new_ll.get(0))
# print(new_ll.get(1))
# print(new_ll.get(2))

# set value at specified position
# print(new_ll.set_value(1, 10))
# print(new_ll.set_value(0, 10))
# print(new_ll.set_value(2, 10))
# new_ll.print_list()


# insert value at specified position
# print(new_ll.insert_value(1, 10).print_list())
# print(new_ll.insert_value(2, 10).print_list())
# print(new_ll.insert_value(0, 10).print_list())
# print(new_ll.insert_value(new_ll.length, 15).print_list())

# remove an element by index
# new_ll.print_list()
# new_ll.remove(1)
# new_ll.print_list()

# reversing ll
# new_ll.print_list()
# new_ll.reverse()
# new_ll.print_list()
