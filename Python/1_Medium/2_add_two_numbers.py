"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        returnList = ListNode(0) # Initiate the linked list with the first entry being a 0 (this will be skipped later)
        current = returnList # create a copy to iterate through creating the linked list such that returnList will remain at the beginning

        carry = 0 # create a carry to handle 2 digit #
        while (l1 or l2) or carry > 0: # While there is SOME value to add
          
            if l1:  # Check if l1 still has values to add
                val1 = l1.val 
                l1 = l1.next
            else: val1 = 0

            if l2: #check if l2 still has values to add
                val2 = l2.val 
                l2 = l2.next
            else: val2 = 0

            sum = val1 + val2 + carry # Sum of carry plus both values
            
            if sum >= 10: # if this results in a number greater than or equal to 10.... 
                sum = sum % 10 # take the module i.e, 15 % 10 = 5
                carry = 1 # take the 10s digit
            else: carry = 0 # otherwise there will be no 10s digit

            current.next = ListNode(sum) # Add value
            current = current.next # iterate to the null next value

        
        return returnList.next # return the returnList WITH SKIPPING the first 0 


if __name__ == '__main__':

    l1_head = ListNode(val = 1, next = ListNode(val = 0, next = ListNode(val = 0, next = ListNode(val = 0, next = ListNode(val = 0, next = ListNode(val = 0, next = ListNode(1)))))))
    l2_head = ListNode(val = 5, next= ListNode(val = 6, next = ListNode(4)))
    
    solution = Solution()
    result = solution.addTwoNumbers(l1_head, l2_head)

    while result:
        print(result.val)
        result = result.next



