from typing import Optional


"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

# assume multiple nodes can have the same value...so haash it?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()

        if head is None:
            return False

        current = head.next

        while current is not None:
            if current in visited:
                return True
            else:
                visited.add(current)
            current = current.next

        return False


        


if __name__ == "__main__":
    solution = Solution()

    # Create nodes
    root = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    # Link nodes together: 1 → 2 → 3 → 4 → 5
    root.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Create the cycle: 5 → 3
    node5.next = node3



    print(solution.hasCycle(root))
