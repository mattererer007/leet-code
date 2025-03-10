"""Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        left_count = 0
        right_count = 0

        if root is None:
            return True
        
        
        root_left = root.left
        root_right = root.right

        queue_left = []
        tag = 0
        queue_left.append((root_left, tag))

        while len(queue_left) > 0:
            node = queue_left.pop(0)
            level = node[2]
            if node[0] is not None:


            return True



        
    def light_switch(self, i: int):
        if i == 0 :
            return 1
        else: 
            return 0

        

if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    print(solution.isBalanced(root))