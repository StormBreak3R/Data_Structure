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

    def search_sll(self, Nodedata):
        if self.head is None:
            print("Empty list")
        else:
            current_node = self.head
            while current_node:
                if current_node.data == Nodedata:
                    print("Found")
                    return
                current_node = current_node.next
            print("Does not exist")


ll = LinkedList()
ll.insertion(10, 0)
ll.insertion(9, 0)
ll.insertion(8, 0)
ll.insertion(11, 1)
ll.insertion(12, 1)
ll.search_sll(12)
