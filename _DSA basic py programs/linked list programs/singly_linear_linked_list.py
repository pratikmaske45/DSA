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



class linkedlist:
    def insert(self, new_node, pos):
        if pos ==1:
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next =temp.next
            temp.next = new_node


    def delete(self, value):
        temp =self.head
        if temp.data ==value:
            self.head=self.head.next
        else:
            while(temp.data!=value and temp): 
                prev =temp
                temp =temp.next
                if temp == None:
                    print("value is not present in the list")
                    return 
                prev.next = temp.next
                temp=None

                      


list =SLL()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.print()    
list.insert(Node(34), 3)
list.delete(10)
list.print()
     



                            
                 