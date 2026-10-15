class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class sll:
    def __init__(self,head=None):
        self.head=head

    def append(self,value):
        temp=node(value)
        if (self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def beg(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp

    def mid(self,value,x):  
        temp=node(value)
        t1=self.head

        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next

    def delt(self,value):
        t1=self.head
        prev=t1
        if(t1.data==value):
            self.head=t1.next
        while(t1.next!=None):
            if (t1.data==value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next

    def reverse(self):
        curr=self.head
        prev=None

        while(curr):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev    

    def print1(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data, end=" ")
            t1=t1.next
        print(t1.data,end=" ")

    def middle(self):
        slow=self.head
        fast=self.head

        while fast != None and fast.next != None:
            slow= slow.next
            fast =fast.next.next 

        if slow != None:
            print("middle", slow.data)
        else:
            print("list is empty")    

    def begdelt(self):
        if self.head==None:
            print("linked list is empty")
        else:
            self.head=self.head.next
                    

obj=sll()
obj.append(10)

obj.append(150)

obj.append(108)

obj.append(104)
obj.beg(50)
obj.beg(100)
obj.mid(600,108)
obj.delt(600)
obj.delt(50)
obj.reverse()
obj.print1()
obj.reverse()
obj.print1()
obj.middle()
obj.begdelt()
obj.print1()
# print sum of two consecutive values