
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)
# Each node is visited only once. A cosntant time O(1) activity is performed to swap. A constant time O(1) activity is used to add the children to queue and repeat
# Runtime dependent entirely on how many nodes there are total 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # check if root has value
        if root is None:
            return 

        # Create queue with root node to start with
        node_stack = deque()
        node_stack.append(root)

        # Iterate as long as there are nodes to parse
        while node_stack:
            # variable to hold current node (LIFO) - DFS
            # If you want queue - FIFO... use .popleft()
            current = node_stack.pop()

            # Check if node present
            if current is not None:
                # Swap the nodes left and right values
                # This needs to be done at the same time or otherwise need another variable to hold one of the values
                current.left, current.right = current.right, current.left                                

                # Add current nodes to 
                node_stack.append(current.left)
                node_stack.append(current.right)

        return root
    
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