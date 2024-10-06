class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.no = 0

    def __len__(self):
        return self.no

    def insert_head(self,value):
        new_node = Node(value)        #create new node
        new_node.next = self.head     #create connection
        self.head =  new_node         #create new node a head node
        self.no += 1

    def append(self, value):   #insert by tail
        new_node = Node(value)   #Step 1: Create a new node with the given value
        if self.head is None: #Empty
            self.head = new_node
            self.no += 1
            return
        # Step 2: Start traversing from the head of the linked list
        curr = self.head
        # Step 3: Traverse through the list until the end is reached (i.e., where curr.next is None)
        while curr.next is not None:  # Traverse the list until you find the last node
            curr = curr.next  # Move to the next node
        # Step 4: Set the 'next' pointer of the last node to the new node
        curr.next = new_node
        self.no += 1

    def insert_after(self, after, value):
        new_node = Node(value)  # Create a new node with the given value
        curr = self.head  # Start traversing from the head of the list
        # Traverse the list until we find the node with the 'after' value or reach the end
        while curr is not None:
            if curr.data == after:  # Check if current node's data matches 'after'
                break
            curr = curr.next  # Move to the next node
        # Case 1: 'after' node is found (curr is not None)
        if curr is not None:
            new_node.next = curr.next  # Link the new node to the next node
            curr.next = new_node  # Link the current node to the new node
            self.no += 1
        else:
            # Case 2: 'after' node is not found (curr is None)
            print('Item not found')

    def clear(self):
        self.head = None
        self.no = 0

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next  #[ [1]self.head, [2]self.next, 3, 4, 6, 5]
            self.no -= 1

        else:
            return 'Empty LinkList'

    def pop(self):
        # Case 1: If the list is empty
        if self.head is None:
            return "Empty list"  # Nothing to pop from an empty list
        # Case 2: If there's only one node in the list
        if self.head.next is None:
            self.head = None  # Remove the single node
            self.no -= 1
            return
        # Case 3: General case - more than one node in the list
        curr = self.head  # Start from the head
        # Traverse the list to reach the second-to-last node
        while curr.next.next is not None:
            curr = curr.next
        # At this point, curr is the second-to-last node
        curr.next = None  # Remove the last node by setting the next reference to None
        self.no -= 1  # Decrease the node count

    def remove(self, value):
        curr = self.head  # Start traversing from the head of the list
        if self.head is None: # Special case: if the list is empty
            return "LinkedList is empty"
        if self.head.data == value: # Special case: if the value to be deleted is in the head node
            self.head = self.head.next  # Move the head to the next node
            self.no -= 1
            return
        # Traverse the list to find the node whose next node has the target value
        while curr.next is not None:  # Continue until the next node is None (end of list)
            if curr.next.data == value:  # Check if the next node's data matches the value to be deleted
                break  # If found, exit the loop
            curr = curr.next  # Move to the next node
        # If we've found the node to delete (curr.next is the node with the target value)
        if curr.next is not None:  # Ensure we aren't at the end of the list (value found)
            curr.next = curr.next.next  # Remove the target node by bypassing it in the list
            self.no -= 1
        else:
            return "Value not found in the Linkedlist"

    def __delitem__(self, index):
        curr = self.head
        pos = 0
        # Case 1: Deleting the head node (index 0)
        if index == 0:
            if self.head is None:
                raise IndexError("Index out of range")
            self.head = self.head.next
            self.no -= 1  # Decrease the count of nodes
            return
        # Case 2: Deleting a node from the middle or end
        prev = None  # This will store the previous node
        while curr is not None:
            if pos == index:
                # Skip the node at the target index by linking previous node to the next node
                prev.next = curr.next
                self.no -= 1  # Decrease the count of nodes
                return
            prev = curr  # Move prev to the current node
            curr = curr.next  # Move to the next node
            pos += 1
        # If index is out of range, raise an error
        raise IndexError("Index out of range")        #

    def search(self, value):
        curr = self.head  # Start from the head of the list
        counter = 0  # To keep track of the index
        while curr is not None:
            if curr.data == value:  # If the value is found
                return counter  # Return the index of the found value
            curr = curr.next  # Move to the next node
            counter += 1  # Increment the index
        # If the loop ends and the value wasn't found
        return 'not found'

    def replace_max(self, value):
        curr  = self.head
        maxi = curr
        while curr is not None:
            if curr.data > maxi.data:
                maxi = curr
            curr = curr.next
        maxi.data = value

    def sum_odd(self):
        curr = self.head
        pos = 0
        add = 0
        while curr is not None:
            if pos%2 != 0:
                add += curr.data
            curr = curr.next
            pos += 1
        return add

    def reverse(self):
        curr = self.head  # Start at the head of the list
        prev = None  # Initialize the previous node to None (this will become the new tail of the list)
        while curr is not None:
            next_node = curr.next  # Save the next node before breaking the link
            curr.next = prev  # Reverse the link: point the current node to the previous node
            # Move forward in the list
            prev = curr  # Move prev to curr (this will eventually become the new head)
            curr = next_node  # Move curr to the next node in the original list (the saved next_node)
        self.head = prev # After the loop, prev will point to the new head of the reversed list

    def __str__(self):  # Traverse the list and return string representation
        curr = self.head  # Start with the head node
        result = ''
        while curr is not None:  # While there are more nodes in the list
            result += str(curr.data) + ' → '
            curr = curr.next
        return result + 'None'  # Mark the end of the list

    def __getitem__(self, index):
        curr = self.head  # Start traversal from the head of the list
        pos = 0  # Initialize a position counter to track the index
        while curr is not None:
            if pos == index:  # If the current position matches the target index
                return curr.data  # Return the data at the current node
            curr = curr.next  # Move to the next node
            pos += 1  # Increment the position counter
        # If the index is out of bounds (list is shorter than index), return None or raise an error
        return 'Index not Found'

    def set_str(self):
        curr = self.head  # Start traversing from the head of the list
        while curr is not None:  # Loop through the entire linked list
            if curr.data == '/' or curr.data == '*':  # If the current node contains '/' or '*'
                curr.data = ' '  # Replace the current node's data with a space ' '
                # Check if the next node contains '/' or '*'
                if curr.next.data == '/' or curr.next.data == '*':
                    # Capitalize the data in the node two steps ahead
                    curr.next.next.data = curr.next.next.data.upper()
                    # Remove the next node by linking the current node directly to the node after next
                    curr.next = curr.next.next
            # Move to the next node in the list
            curr = curr.next

l = Linkedlist()
# l.append('T')
# l.append('h')
# l.append('e')
# l.append('/')
# l.append('*')
# l.append('s')
# l.append('k')
# l.append('y')
# l.append('/')
# l.append('i')
# l.append('s')
# l.append('/')
# l.append('/')
# l.append('b')
# l.append('l')
# l.append('u')
# l.append('e')
# l.set_str()
l.append(2)
l.append('Hello')
l.append(12)
l.append('is')
l.append(93)
l.append(32)
print(l)
# print(l)
# l.replace_max(55)
print(l)
# print(l.sum_odd())
# l.reverse()
print(l)


# ll.insert_after(40,42)
# # ll.clear()
# print(ll)
# ll.delete_head()
# print(ll)
# ll.pop()
# print(ll)
# ll.remove(25)
# ll.append(46)
# ll.append(6*6)
# ll.append(77)
# print(ll)
# print(ll.search(77))
# print(ll[4])
# print(ll)
# del ll[4]
# print(ll)

# print()
# a = Node(1)
# b = Node(2)
# c = Node(3)
# print('a',id(a))
# print('b',id(b))
# print('c',id(c))
# a.next = b
# b.next = c
# print(a.next)
# print(b.next)
# print('c.next',c.next)
# print(int(id(a.next)))
# print(int(id(b.next)))
# print(int(id(c.next)))