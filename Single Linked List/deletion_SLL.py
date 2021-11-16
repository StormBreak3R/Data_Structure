class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, data, loc):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if loc == 0:
                new_node.next = self.head
                self.head = new_node
            elif loc == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                tmp_node = self.head
                index = 0
                while index < loc - 1:
                    tmp_node = tmp_node.next
                    index += 1
                next_node = tmp_node.next
                tmp_node.next = new_node
                new_node.next = next_node

    def show(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            current_node = self.head
            a = []
            while current_node:
                a.append(current_node.data)
                current_node = current_node.next
            print(a)

    def deletion(self, loc):
        if self.head is None:
            print("list already empty")
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    beforeLast_node = self.head
                    while beforeLast_node:
                        if beforeLast_node.next == self.tail:
                            break
                        beforeLast_node = beforeLast_node.next
                    beforeLast_node.next = None
                    self.tail = beforeLast_node
            else:
                tmp_node = self.head
                index = 0
                while loc < loc - 1:
                    tmp_node = tmp_node.next
                    index += 1
                next_node = tmp_node.next
                tmp_node.next = next_node.next


ll = LinkedList()
ll.insertion(10, 0)
ll.insertion(9, 0)
ll.insertion(8, 0)
ll.insertion(11, 1)
ll.insertion(12, 1)
ll.show()
ll.deletion(0)
ll.show()