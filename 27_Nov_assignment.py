class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    cnt = 0 
    def __init__(self):
        self.root = None

    def append(self,new_node):
        if self.root is None:
            self.root = new_node
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
        self.inorder(rt.left)
        print(rt.data , end = " ")
        self.inorder(rt.right)

    def findminmax(self,rt):
        temp = rt 
        while temp.left is not None:
            temp = temp.left
        print("\nmin score is:", temp.data)
        temp = rt
        while temp.right is not None:
            temp = temp.right
        print("max score is:",temp.data)

    def fifty(self,rt):
        if rt is None:
            return 
         
        else:
            if  rt.data > 50:
                self.cnt +=1
            self.fifty(rt.left)
            self.fifty(rt.right)

    def search(self,x):
        temp = self.root 
        while temp:
            if temp.data == x:
                return True
            elif x < temp.data:
                temp = temp.left
            else:
                temp = temp.right 
        return False 
        
    def sum(self,rt):
        if rt is None:
            return 0
        else:
            return rt.data + self.sum(rt.left) + self.sum(rt.right)
    
    def count(self,rt):
        if rt is None:
            return 
        else:
            self.count(rt.left)
            self.cnt += 1
            self.count(rt.right)

    def leaf(self,rt):
        if rt is None:
            return 
        if rt.left is None and rt.right is None:
            self.cnt +=1 
        self.leaf(rt.left)
        self.leaf(rt.right)

    def nleaf(self,rt):
        if rt is None:
            return 
        if rt.left is not None or rt.right is not None:
            self.cnt += 1
        self.leaf(rt.left)
        self.leaf(rt.right)

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        else:
            arr = []
            cnt = 0 
            arr.append(rt)
            while(cnt<len(arr)):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end= " ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)   

    def delete(self,rt,value):
        if rt is None:
            return 
        if value < rt.data:
            rt.left = self.delete(rt.left,value)
        elif value > rt.data:
            rt.right = self.delete(rt.right,value)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left
        
            succ = self.successor(rt)
            rt.data = succ.data
            rt.right = self.delete(rt.right,succ.data)
        return rt 
    def successor(self,temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp 
            
         
        


b1 = BST()

scores = [45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98]
for i in scores:
    b1.append(Node(i))
print("scores in ascending order are:")
b1.inorder(b1.root)
b1.findminmax(b1.root)
b1.cnt = 0 
b1.fifty(b1.root)
print("The scores greater than 50 are:",b1.cnt)
x = 45
if b1.search(x):
    print("the score is present:",x)
else:
    print(x,"score is not present")
b1.cnt = 0 
total = b1.sum(b1.root)
b1.count(b1.root)

avg = total / b1.cnt 
print("average of scores is:",avg)

b1.cnt = 0
b1.leaf(b1.root)
print("the no. of leaf nodes are:",b1.cnt)

b1.cnt = 0 
b1.nleaf(b1.root)
print("the no. of non leaft nodes are:", b1.cnt)
print("The level order is:")
b1.level_order(b1.root)
print("\nafter deletion:")
print("after deletion:")
b1.root = b1.delete(b1.root,98)
b1.inorder(b1.root)