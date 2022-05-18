class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        arr = []
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        print(arr)

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return True
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return True


# Creating a queue
queue = Queue(4)
# queue.print_queue()

# enqueue
#
queue.enqueue(10)
queue.print_queue()
# queue.enqueue(12)
# queue.print_queue()
# dequeue
# queue.dequeue()
queue.print_queue()

# dequeue
queue.dequeue()
queue.print_queue()
queue.dequeue()
queue.print_queue()
