# singly linear linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:    
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp =temp.next

list =SLL()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.print()            
                            
                 