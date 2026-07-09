from typing import Optional

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""

# First solution >> iterate through list and count number of nodes than iterate again to print whatever is the middle node 
# O(n) time complexity O(1) space complexity

# Second solution >> have a fast and short pointer where F jumps two at time whileslow jumps 1
# Once at end of list, the slow pointer will be at the middle...but will it be at the second middle node I don't think so

# I am going to go with the first solution 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0

        # find the middle node
        current = head        
        while current:
            count += 1
            current = current.next

        middle = (count) // 2
        print(middle)

        # return middle node
        middle_node = head
        while middle > 0:
            middle -= 1
            middle_node = middle_node.next

        return middle_node
            
    

if __name__ == "__main__":
    solution = Solution()

    head = ListNode(val = 0, next = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3))))

    print(solution.middleNode(head))