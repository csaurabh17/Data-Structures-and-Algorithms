class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        arr = []
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        print(arr)

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height = 1
            return True
        temp = self.top
        self.top = new_node
        new_node.next = temp
        self.height += 1
        return True

    def pop(self):
        temp = self.top
        if self.top is None:
            return None
        elif self.height == 1:
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp.value

# Creating a stack
stack = Stack(4)
stack.print_stack()

# Push
stack.push(10)
stack.push(12)
stack.print_stack()

# Pop
# stack.pop()
# stack.print_stack()

