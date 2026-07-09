import math

"""Given the root of a binary tree, invert the tree, and return its root.
right branch > left branch

Assume that each level is full binary

left = 2k +1
right = 2k + 2

root = [4,2,7,1,3,6,9] -> Output = [4,7,2,9,6,3,1]
"""


""""Edge Cases:
(1) empty tree -> returns empty tree?

"""


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Essentially every node BUT the root needs to be swapped...real easy. Create a queue and iterate through
    the entire list. Queue is nice because first in first out means you can go level by level
    
    """
    def invertTree(self, root: TreeNode) -> TreeNode:

        # If no TreeNode provided....return None
        if root is None:
            return None
        
        # Create a copy of root to iterate through
        temp = root
        #  Create queue for nodes whose children may or may not need to be pulled
        queue = []
        # Start with root
        queue.append(temp)

        # While there are items (nodes) in queue...
        while len(queue) > 0:
            node = queue.pop(0) # Pull top node off of queue
                        
            if node is not None: # If the exists and you have not reached the children of a leaf
                node.left, node.right = node.right, node.left # Swap sides
                queue.append(node.left) # add sides to queue so that their children can be swapped
                queue.append(node.right)

        return temp # Return new list


    def print_tree(self, root):
        if not root:
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
    

if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    solution.print_tree(root)
    result = solution.invertTree(root)
    solution.print_tree(result)
        

    

