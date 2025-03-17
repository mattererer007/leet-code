"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Definition “The lowest common ancestor is defined between two nodes p and q as the lowest node in
T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return
    
if __name__ == "__main__":

    # Level 0
    root = TreeNode(6)

    # Level 1
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    # Level 2
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    # Level 3
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    solution = Solution()
    print(solution.lowestCommonAncestor(root = root, p = root.left, q = root.right))