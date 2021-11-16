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
                a.append("->")
                current_node = current_node.next
            print(a)


    def user_input(self):
        for i in range(int(input('how many numbers you want to insert: '))):
            ll.insertion(loc=int(input("location: ")), data=int(input("data: ")))


ll = LinkedList()
ll.user_input()
ll.show()
