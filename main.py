class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        new = Node(data=data)
        if(self.head):
            temp = temp.next
            while temp.next != None:
                temp = temp.next
            temp.next = new
        else:
            self.head = new