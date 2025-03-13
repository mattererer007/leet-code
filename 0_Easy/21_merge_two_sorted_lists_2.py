from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

- lists can be different lengths
- lists are always sorted
- list can be blank
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
       
        # Create copy of head to use as a pointer to add more values
        head_copy = head

        while list1 and list2: 
            if list1.val < list2.val:
                head_copy.next = list1
                list1 = list1.next
            else:
                head_copy.next = list2
                list2 = list2.next
            head_copy = head_copy.next

        if list1:
            head_copy.next = list1
        if list2:
            head_copy.next = list2

        return head.next

    
if __name__ == "__main__":

    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next = None)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))


    solution = Solution()
    result = solution.mergeTwoLists(list1=list1, list2=list2)

    while result != None:
        print(result.val)
        result = result.next

    