class Node:
    data : int
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_linked_list:
    def __init__(self):
        self.head = None
    
    def insert_first(self,c_head):
        if not self.head:
            self.head = c_head
            c_head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = c_head
            c_head.next = self.head
            self.head = c_head
        
    def insert_middle(self,center,add_node):
        add_node.next = center.next
        center.next = add_node
        
    def insert_end(self,add_node):
        if not self.head:
            self.insert_first(add_node)
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        add_node.next = temp.next
        temp.next = add_node
        
    def delete_first(self):
        if not self.head:
            return
        if self.head == self.head.next:
            self.head = self.head.next = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
        
    def delete_middle(self,delete_node):
        if not self.head or self.head == self.head.next:
            return
        if delete_node == self.head:
            self.delete_first()
            return
        before = self.head
        while before.next != delete_node:
            before = before.next
            if before == self.head:
                return
        before.next = delete_node.next
        
    def delete_end(self):
        if not self.head:
            return
        if self.head == self.head.next:
            self.head = self.head.next = None
            return
        before = self.head
        while before.next.next != self.head:
            before = before.next
        before.next = self.head
        
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(f"{temp.data}->", end="")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")
