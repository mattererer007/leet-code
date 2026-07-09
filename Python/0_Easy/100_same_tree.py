from typing import Optional
from collections import deque

"""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS solution - fast but memory intensive
# O(m + n) where m = nodes, n = edges
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # create a queue to iterate level by level 
        p_queue = deque([p])
        q_queue = deque([q])

        # While there are nodes to review in either...
        while p_queue or q_queue:
            current_p = p_queue.popleft()
            current_q = q_queue.popleft()

            # Check if none or if they are not the same
            check = self.checkVal(current_p, current_q)

            if not check:
                return False

            # Pull in the same order, the left node and the right node
            if current_p is not None:
                p_queue.append(current_p.left)
                p_queue.append(current_p.right)

            if current_q is not None:
                q_queue.append(current_q.left)
                q_queue.append(current_q.right)

        return True
    
    def checkVal(self, current_p: Optional[TreeNode], current_q: Optional[TreeNode]) -> bool:

        if current_p is None and current_q is None:
            return True
        elif current_p is None and current_q is not None:
            return False
        elif current_q is None and current_p is not None:
            return False
        elif current_p.val != current_q.val:
            return False
        else:
            return True
        
class Solution2:
    def recursionIsSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p==None and q==None):
            return True
        if(p==None or q==None):
            return False
        if(p.val!=q.val):
            return False
        a=self.recursionIsSameTree(p.left,q.left)
        b=self.recursionIsSameTree(p.right,q.right)
        
        # return combination of booleans (T +T = T, T + F = F, F + F = F)
        return a and b


if __name__ == "__main__":
    # Level 1 (root)
    root1 = TreeNode(1)
    root2 = TreeNode(1)

    # Level 2
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    # Level 3
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)

    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)

    solution = Solution()
    print(solution.isSameTree(root1, root2))