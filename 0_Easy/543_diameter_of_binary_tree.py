from typing import Optional

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time complexity with 'n' being the number of nodes O(h) space complexity with the recursion stack being the heigh of the binary tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Set global variable for class
        global largest_diameter
        largest_diameter = 0

        def depth(root):
            # pull in global variable 
            global largest_diameter

            if root is None:
                return 0
            
            # pull in the max depth of path way
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            # Take the diameter at each step
            diameter = left_depth + right_depth
            
            # find the largest
            largest_diameter = max(largest_diameter, diameter)
        
        
            # iterate through all nodes return which pathway returns max depth
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return(largest_diameter)
    

if __name__ == "__main__":

    solution = Solution()

# Constructing the tree:
#
#           1
#         /   \
#        2     3
#       / \     \
#      4   5     6
#         /
#        7
#       /
#      8


# DFS to the end of a path
## depth(1) >> depth(2), depth(3)
### depth(2) >> depth(4), depth(5)
### depth(3) >> depth(6)
#### depth(4)
#### depth(5) >> depth(7)
#### depth(7) >> depth(8)


# node = 8, 8.left = 0, 8.right = 0 >> diameter = 0, max_d = (0,0) >> return 1 + max(0,0) == 1
# node = 7, 7.left = 1, 7.right = 0 >> diameter = 1, max_d = (0,1) >> return 1 + max(1,0) == 2
# node = 5, 5.left = 2, 5.right = 0 >> diameter = 2, max_d = (1,2) >> return 1 + max (2,0) == 3
# node = 4, 4.left = 0, 4.right = 0 >> diameter = 0, max_d = (2,0) >> return 1 + max(0,0) == 1
# node = 2, 2.left = 1, 2.right = 3 >> diameter = 4, max_d = (2,4) >> return 1 + max(1,3) == 4
# node = 6, 6.left = 0, 6.right = 0 >> diameter = 0, max_d = (4,0) >> return 1 + max(0,0) == 1
# node = 3, 3.left = 0, 3.right = 1 >> diameter = 1, max_d = (4,1) >> return 1 + max(0,1) == 2
# node = 1, 1.left = 6, 1.right = 2 >> diameter = 7, max_d = (4,6) >> return 1 + max(4,2) == 5

    node8 = TreeNode(8)
    node7 = TreeNode(7, left=node8)
    node6 = TreeNode(6)
    node5 = TreeNode(5, left=node7)
    node4 = TreeNode(4)
    node3 = TreeNode(3, right=node6)
    node2 = TreeNode(2, left=node4, right=node5)
    root = TreeNode(1, left=node2, right=node3)

    print(solution.diameterOfBinaryTree(root))