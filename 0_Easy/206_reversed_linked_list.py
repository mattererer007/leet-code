from typing import Optional
from collections import deque

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        lifo = []
        current = head


        while current:
            lifo.append(current)
            current = current.next

        x = lifo.pop()
        return_head = x
        while lifo and x is not None:
            y = lifo.pop()
            if y:
                y.next = None
                x.next = y
                x = x.next

        
        
        return return_head




        

if __name__ == "__main__":
    
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    output = solution.reverseList(head)
    
    while output:
        print(output.val)
        output = output.next