class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def Insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        standard = self.root
        while True:
            if data < standard.data:
                if standard.left is None:
                    standard.left = Node(data)
                    break
                else:
                    standard = standard.left
            elif data > standard.data:
                if standard.right is None:
                    standard.right = Node(data)
                    break
                else:
                    standard = standard.right
            else:
                break

    def Find(self, data):
        standard = self.root
        while standard is not None:
            if data < standard.data:
                standard = standard.left
            elif data > standard.data:
                standard = standard.right
            else:
                return standard
        return None

    def FindParent(self, node):
        parent = None
        current = self.root
        while current is not None:
            if current is node:
                return parent
            elif node.data < current.data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return None

    def FindSuccessor(self, standard):
        result = standard.right
        while result.left is not None:
            result = result.left
        return result

    def replace(self, parent, node, new_node):
        if parent is None:
            self.root = new_node
        elif parent.left is node:
            parent.left = new_node
        else:
            parent.right = new_node

    def Remove(self, data):
        standard = self.Find(data)
        if standard is None:
            return

        if standard.left is not None and standard.right is not None:
            successor = self.FindSuccessor(standard)
            standard.data = successor.data
            parent_of_succ = self.FindParent(successor)
            self.replace(parent_of_succ, successor, successor.right)
        elif standard.left is not None:
            parent = self.FindParent(standard)
            self.replace(parent, standard, standard.left)
        elif standard.right is not None:
            parent = self.FindParent(standard)
            self.replace(parent, standard, standard.right)
        else:
            parent = self.FindParent(standard)
            self.replace(parent, standard, None)


T = Tree()
for i in [40,20,60,30,70,10,50]:
    T.Insert(i)

T.Remove(20)
T.Remove(60)
T.Remove(10)
T.Remove(70)