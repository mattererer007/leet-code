"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

All Node.val are unique.
p != q
p and q will exist in the BST.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root

if __name__ == "__main__":

    solution = Solution()

    root = TreeNode(6)
    root.left = TreeNode(2)
    p = root.left
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    q = root.left.right
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    print(solution.lowestCommonAncestor(root,p,q))

