"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

All Node.val are unique.
p != q
p and q will exist in the BST.
"""

## Key thing to recall is that a BST is sorted. Left of a node than node and Right of a node is > node
#### Based on root node

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(h) runtime complexity given that only one node is being appraised at each level. O(1) space complexity
# as no new variables, lists/queues/stacks are created to help iterate through the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        current = root

        while current:
            # if both values fall to right of current node
            if p.val > current.val and q.val > current.val:
                current = current.right
            # if both values fall to left of current node
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # find a situation where the current node is either p or q or the last node before the nodes split off
            elif min(p.val, q.val) <= current.val and max(p.val, q.val) >= current.val:
                return current.val
            

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
    q = root.right.right


    print(solution.lowestCommonAncestor(root,p,q))

