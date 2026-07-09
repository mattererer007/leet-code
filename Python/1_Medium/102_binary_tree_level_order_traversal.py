from typing import Optional, List
from collections import deque

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time complexity O(n) space complexity for storing queue in lsits before appraisal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Check for blank list
        if not root:
            return []
        
        # Create a queue to iterate through each level of the binary tree using BFS
        queue = deque()
        queue.append([root]) # Initaite with root in a list
        output = [] # output will eb a list of lists of ints

        # While there are levels in the binary tree with non-Null nodes...
        while queue:
            # Take 1 tier at a time. Tier being all nodes at a certain level within tree
            tier = queue.popleft()
            
            level = [] # To collect int values from level
            next_level = [] # to prepare next level of tree
            while tier: # while ndoes at a tier
                node = tier.pop(0) # iterate one node at a time
                level.append(node.val) # add int value to level for output

                # if node has non-Null children...add to next level of examination
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            # Append the completed level of int values
            output.append(level)

            # If there are valide ndoes to continue to review...add
            if next_level:
                queue.append(next_level)

        return output


    
if __name__ == "__main__":
    
    solution = Solution()

    root = TreeNode(val=3, left=TreeNode(val = 9, left = None, right = None), right = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7)))

    print(solution.levelOrder(root))