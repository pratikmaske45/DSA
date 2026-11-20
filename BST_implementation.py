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
    def inorder(self,rt):
        if rt is None:
            return 
        else:
            self.inorder(rt.left)
            print(rt.data, end = " ")
            self.inorder(rt.right)
    print("Inorder:")

    def preorder(self,rt):
        if rt is None:
            return 
        else:
            print(rt.data, end = " ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self,rt):
        if rt is None:
            return 
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end = " ")

    def findminmax(self,rt):
        temp = rt
        while temp.left is not None:
            temp=temp.left
        print("minimum value in BST is:", temp.data)
        temp = rt 
        while temp.right is not None:
            temp = temp.right
        print("maximum value in BST is:", temp.data)
b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.inorder(b1.root)
print("\npreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)
print("\nMinimum and Maximum value in BST is:")
b1.findminmax(b1.root)           
    
        
          
