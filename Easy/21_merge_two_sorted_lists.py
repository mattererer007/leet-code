"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    
        # Initiate a new node that will take the location of other nodes to create merged list
        head = ListNode() 
        
        # Create pointer that will iterate through the items bein added so that head will will be at
        # beginning og the merged linked list
        current = head

        # iterate through until one list is exhausted (best practice since you just need to link the rest of 
        # non-exhausted list at the end)
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # set 'next' to list1 
                list1 = list1.next
            else:
                current.next = list2 # set 'next' to list2 
                list2 = list2.next
            current = current.next # iterate to the value just selected as next in line (either list1 node or list2)
            # essentially this whole approach relies on pointers to the space in memory where an individual node is held

        # Once one list is exhausted, go ahead and simply set the rest of the non exhausted 
        # list to the end of the merged list
        current.next = list1 or list2 
        return head.next # You return this instead of head since head has a val of 0 based on initiating an empty node
            

# Test case
if __name__ == "__main__":
    
    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next = None)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

    solution = Solution()
    result = solution.mergeTwoLists(list1=list1, list2=list2)

    while result != None:
        print(result.val)
        result = result.next
        