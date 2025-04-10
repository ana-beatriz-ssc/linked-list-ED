from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                        previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
    
    def display(self):
        current = self.head

        while current:
            print(current.data,  end="->")
            current = current.next
        print("None")