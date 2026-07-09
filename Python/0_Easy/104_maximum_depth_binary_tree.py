from typing import Optional
"""
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# O(n) time and O(n) space complexity
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Set the layer of the binary tree to zero initially
        level = 0

        # Check if there are any TreeNodes in root
        if not root:
            return level

        # Set current layer to root
        current = {}
        current[level] = [root]

        # While there are still TreeNodes in a layer...
        while len(current[level]) > 0:

            # Set up new layer
            level += 1
            current[level] = []

            # Iterate through old layer and see if there are any nodes 1 layer down
            for x in current[level-1]:
                if x.left is not None:
                    current[level].append(x.left)
                if x.right is not None:
                    current[level].append(x.right)
        
        return level

# DFS
# O(n) time and O(n) space complexity    
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # iterate through all nodes return which pathway returns max depth
        return 1 + max(left_depth, right_depth)
                    


    
if __name__ == "__main__":

    solution = Solution()

    root = TreeNode(val = 0, left = TreeNode(val=1, left = TreeNode(val=3, left = TreeNode(val=4))), right = TreeNode(val = 2))

    print(solution.maxDepth(root))
