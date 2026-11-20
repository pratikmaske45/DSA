# BST using linked list 
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None: # Tree is empty (No node in BST)
            self.root=new_node
        else:
            temp = self.root 
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return 
                    else:
                        temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return 
                    else:
                        temp = temp.right 

    
        
          
