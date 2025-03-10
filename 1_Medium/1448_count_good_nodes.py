"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes_nonrecursive(self, root: TreeNode) -> int: # O(n) runtime as each node is visited ONCE

        good_nodes = 0 # initiate count

        stk = [(root, float('-inf'))] # Utilize a stack (Last In First Out) with a tuple with the node and the current max value
        # Basically to solve this problem, you need to compare the value of each node to the largest value up until that point.
        # There is NO global max. Rather for a node to be good it must be >= than all the nodes from the root to itself 
        # Thus need to constantly check in on what the largest (LOCAL) value value is 

        while stk:
            node, largest_val = stk.pop() # take the last item added to the stack

            if node.val >= largest_val: # If value is greater than or equal the current max...increase good node count
                good_nodes += 1

            largest_val = max(largest_val, node.val) # Determine what is the largest value now

            if node.left: stk.append((node.left, largest_val)) # Add left node to stack (if it is NOT none)
            if node.right: stk.append((node.right, largest_val)) # Add right node to stack (if it is NOT none)


        return good_nodes
    
    def goodNodes_recursive(self, root: TreeNode) -> int: # At the best, the runtime is O(log(n)) assuming it is a well-balanced tree....otherwise it is O(n) 

        good_nodes = self.dfs(root, float('-inf')) # initiate dfs 

        return good_nodes
    
    def dfs(self, root: TreeNode, maxVal: int) -> int:
        if not root: # if there is no Nodesm return 0
            return 0

        good_nodes = 1 if root.val >= maxVal else 0 # good_nodes is set to 1 if the current node value is greater than or equal to current max_val

        maxVal = max(maxVal, root.val) # reassess max value

        # proceed with recursion 
        good_nodes += self.dfs(root.left, maxVal) #DFS on left node
        good_nodes += self.dfs(root.right, maxVal) #DFS on right node 

        return good_nodes
        

if __name__ == '__main__':
    
    solution = Solution()
    
    root = TreeNode(val = 3, left= TreeNode(val = 1, left = TreeNode(val = 3)), right=TreeNode(4, left = TreeNode(1), right = TreeNode(4)))

    print(solution.goodNodes_nonrecursive(root))
    print(solution.goodNodes_recursive(root))

    