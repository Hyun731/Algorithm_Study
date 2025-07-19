class Node:
    data : int
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_first(self,c_head):
        c_head.next = self.head
        if self.head:
            self.head.prev = c_head
        else:
            self.tail = c_head
        self.head = c_head
        
    def insert_middle(self,center,add_node):
        add_node.next = center.next
        add_node.prev = center
        if add_node.next:
            add_node.next.prev = add_node
        else:
            self.tail = add_node
        center.next = add_node
        
        
    def insert_end(self,add_node):
        if not self.head:
            self.head = self.tail = add_node
        else:
            self.tail.next = add_node
            add_node.prev = self.tail
            self.tail = add_node
        
    def delete_first(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        
    def delete_middle(self,delete_node):
        delete_node.prev.next = delete_node.next
        if delete_node.next:
            delete_node.next.prev = delete_node.prev
        else:
            self.tail = delete_node.prev
            
        
    def delete_end(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data}<->", end="")
            temp = temp.next
        print("NULL")
        
D = Double_linked_list()
