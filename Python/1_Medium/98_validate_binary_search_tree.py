from typing import Optional

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left of a node contains only nodes with keys less than the node's key.

The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time complexity where n are number of nodes in tree
# O(k) space complexity where k is the number of levels placed onto recursion stack before a False is returned. At worse n=k
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        

        def dfs(node: Optional[TreeNode], min, max) -> bool:

            # If a None value is reached then no further nodes to trace, return True
            if not node:
                return True
            
            # If the node provided is between the min and max, continue...otherwise return False
            if not (min < node.val < max):
                return False
            else:
                # For left nodes, must be less than parent value and greater than min 
                # For right nodes, must be less than max and greater than parent 
                ## this results in a situation where the left most node has a min of -inf and the right most node in the tree has a max of inf
                ## node.val from the beginning creates a dividing line based ont he root value to ensure that both sides of the tree do not cross it
                return dfs(node=node.left, min=min, max=node.val) and dfs(node=node.right, min=node.val, max=max)


        # Initiate the root with an unlimited low and high as the root can be any value
        return dfs(node=root, min=float('-inf'), max=float('inf'))
    

if __name__ == "__main__":

    root = TreeNode(val = 5, left = TreeNode(val=4), right = TreeNode(val=6, left = TreeNode(val=3), right=TreeNode(val=7)))


    solution = Solution()
    print(solution.isValidBST(root))