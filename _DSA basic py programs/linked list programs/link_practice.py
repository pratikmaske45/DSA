# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             print("The linked list is created:-")
#             return

#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = new_node
#     def traverse(self):
#         current =self.head
#         print("The list elements are:")
#         while current is not None:
#             print( current.data, end = " -> ")
#             current = current.next 
#         print(None)    



# my_list = LinkedList()
# my_list.append(10)                  
# my_list.append(20)                  
# my_list.append(30)                  
# my_list.traverse()





class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("The linked list is created:-")
            return 

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
# traversing the list 
    def traverse(self):
        current = self.head 
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print(None)
# insert at beginning 
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node 

# deleting the first node
    def del_begin(self):
        if self.head is not None:
            self.head = self.head.next

   
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("Original List:")
my_list.traverse()

my_list.insert_begin(5)
print("The list after inserting value at first position:")
my_list.traverse()

my_list.del_begin()
print("The list after deleting the first node:")
my_list.traverse()
