class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None
    def add(self, node):
        newnode=Node(node)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def viewll(self):
        curr=self.head
        while curr:
            print(curr.val, end=" ")
            curr=curr.next
        print()
    def delelement(self, node):
        curr=self.head
        if curr.val==node:
            curr.val=curr.next.val
        curr.next=curr.next.next
        


solve=LinkedList()
solve.add(3)
solve.add(4)
solve.add(5)
solve.viewll()
solve.delelement(3)
solve.viewll()
# class Node:
#     def __init__(self, val, next=None):
#         self.val=val
#         self.next=next
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#
#     def add(self, node):
#         newnode=Node(node)
#         if not self.head:
#             self.head=newnode
#         else:
#             curr=self.head
#             while curr.next:
#                 curr=curr.next
#             curr.next=newnode
#     def addatBeginning(self, node):
#         newnode=Node(node)
#         if not self.head:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head=newnode
#
#
#     def viewll(self):
#         curr=self.head
#         while curr:
#             print(curr.val, end=" ")
#             curr=curr.next


# solve=LinkedList()
# solve.add(3)
# solve.add(4)
# solve.add(5)
# solve.add(7)
# print("before adding at beginning ")
# print(solve.viewll())
# print("after adding 2 at beginning ")
# solve.addatBeginning(2)
# print(solve.viewll())
# print("after adding 99 at beginning ")
# solve.addatBeginning(99)
# print(solve.viewll())