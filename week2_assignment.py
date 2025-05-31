class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            print("List is empty. Cannot delete.")
            return

        if n < 1:
            print("Invalid index. Please use a positive integer.")
            return
        
        temp = self.head

        if n == 1:
            self.head = self.head.next
            return

        prev = None
        count = 1
        
        while temp and count < n:
            prev = temp
            temp = temp.next
            count += 1
        
        if not temp:
            print("Index out of range. No deletion performed.")
            return
        
        prev.next = temp.next

ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Original List:")
ll.print_list()

ll.delete_nth_node(2)

print("List after deleting 2nd node:")
ll.print_list()


