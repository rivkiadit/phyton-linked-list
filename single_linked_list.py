class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def  add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_front(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
linked_List = LinkedList()

linked_List.add_to_front(3)
linked_List.add_to_front(2)
linked_List.add_to_front(1)

linked_List.add_to_end(3)
linked_List.add_to_end(3)
linked_List.add_to_end(3)

print("Linked list awa: ")
linked_List.print_lingked_list()
linked_List.remove_front()
linked_List.remove_end()

print("Linked list setelah penghapusan: ")
linked_List.print_lingked_list()