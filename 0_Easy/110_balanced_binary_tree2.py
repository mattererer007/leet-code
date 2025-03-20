from typing import Optional
from collections import deque

"""
Given a binary tree, determine if it is .


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        left_queue = deque([(root.left, 1)])
        right_queue = deque([(root.right, 1)])


        while left_queue or right_queue:

            if left_queue:
                left, left_level = left_queue.popleft()
                if left:
                    left_queue.append((left.left, left_level + 1))
                    left_queue.append((left.right, left_level+ 1))
            
            if right_queue:
                right , right_level= right_queue.popleft()
                if right:
                    right_queue.append((right.left, right_level + 1))
                    right_queue.append((right.right, right_level + 1))

        
            if abs(left_level - right_level) > 1:
                return False
            
        return True         
            


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    solution = Solution()
    print(solution.isBalanced(root))