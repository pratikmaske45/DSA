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


    def traverse(self):
        current = self.head 
        print("The list elements are:")
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next 
        print(None)


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.traverse()