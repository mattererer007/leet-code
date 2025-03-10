"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

ASSUMPTIONS:P != q, p and q will exist in BST, p or q could be the parent of the other 


"""


"""
MY ORIGINAL SOLUTION

# find parents for p [] , q {}
        temp = root
        p_list = []
        p_list.append(temp) 
        while temp.val != p.val:
            if temp.val < p.val:
                temp = temp.right
            else: 
                temp = temp.left
            p_list.append(temp)


        # find dict for q
        temp = root
        q_dict = {}
        q_dict[temp] = ""
        while temp.val != q.val:
            if temp.val < q.val:
                temp = temp.right
            else: 
                temp = temp.left
            q_dict[temp] = ""

        for x in range(len(p_list)-1,-1, -1):
            if p_list[x] in q_dict:
                return p_list[x]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # O(H) runtime
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root is not None:
            if p.val > root.val and q.val > root.val: # Situation where both of the values may be found in the right half of graph
                root = root.right
            elif p.val < root.val and q.val < root.val: # Situation where both of the values may be found in the left half of graph
                root = root.left
            else: return root # lowest node such that it is the parent of both


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


    # temp = root
    # queue = []
    # queue.append(temp)
    # while len(queue) > 0:
    #     node = queue.pop(0)
    #     if node is not None:
    #         print(node.val)
    #         queue.append(node.left)
    #         queue.append(node.right)

    value = solution.lowestCommonAncestor(root, p , q)
    print(value.val)
        
