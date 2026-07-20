from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if not root:
            return []

        inverse_tree = root
        
        stack = [inverse_tree]
        row_stack = []

        while len(stack) > 0:

            node = stack.pop()

            if node is not None:
                row_stack.append(node.left)
                row_stack.append(node.right)

                sub_node_to_left = row_stack.pop()
                sub_node_to_right = row_stack.pop()
                node.left = sub_node_to_left 
                node.right = sub_node_to_right

                stack.append(node.left)
                stack.append(node.right)
        
        return root
            
 

    def print_tree(self,root: TreeNode) -> list[int]:
        if root is None:
            return []
        
        output = [root.val]

        children = deque([root.left, root.right])

        while len(children) > 0:
            child = children.popleft()

            if child is not None:
                output.append(child.val)
                children.append(child.left)
                children.append(child.right)

        return output        


if __name__ == "__main__":
    solution = Solution()


    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(solution.print_tree(root))
    result = solution.invertTree(root)
    print(solution.print_tree(result))