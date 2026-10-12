
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)

        self.head = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

    # 2. Traverse and print
    def traverse(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert node at position 3
    def insert(self, data, pos):
        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete node at position 2
    def delete(self, pos):
        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        temp.next = temp.next.next

    # 6. Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 7. Sum of consecutive node values
    def pair_sum(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            print(temp.data + temp.next.data)
            temp = temp.next


# Main program
s = SLL()

s.create()

print("Original Linked List:")
s.traverse()

print("\nAfter Inserting 25 at Position 3:")
s.insert(25, 3)
s.traverse()

print("\nMiddle Node:")
s.middle()

print("\nAfter Deleting Node at Position 2:")
s.delete(2)
s.traverse()

print("\nReversed Linked List:")
s.reverse()
s.traverse()

print("\nSum of Consecutive Nodes:")
s.pair_sum()

