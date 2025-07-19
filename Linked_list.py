class Node:
    data : int
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_first(self,c_head):
        c_head.next = self.head
        self.head = c_head
        
    def insert_middle(self,center,add_node):
        add_node.next = center.next
        center.next = add_node
        
    def insert_end(self,add_node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = add_node
        
    def delete_first(self):
        self.head = self.head.next
        
    def delete_middle(self,delete_node):
        before = self.head
        while before.next != delete_node:
            before = before.next
        before.next = delete_node.next
        
    def delete_end(self):
        before = self.head
        while before.next.next != None:
            before = before.next
        before.next = None
        
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("NULL")

L = Linked_list()
