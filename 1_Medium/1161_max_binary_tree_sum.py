"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
clear
"""



from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: # O(n) as every node is explored only once 
        max_sum = (float('-inf'), 0) # Since we need to show the level where the max sum is found, need to track both max sum and level that max is found on
        level = 1 # Per instructions root begins at level 1


        queue = [root] # initiate a queue with the initial node
        while queue: # while there are still nodes to explore....
            sum = 0 # local sum per level
            nodes_in_level = len(queue) # how many nodes are found at this specific level (i.e., for root....just 1)

            for x in range(0, nodes_in_level): # count out the number of nodes in a level to ensure that only the nodes of that level are used to find sum

                current = queue.pop(0) # per queue logic First In...First Out (could also use deque here but whatevs)

                sum += current.val # sum the value of each node at a given level

                # see if there are more nodes one level down to explore
                if current.left: queue.append(current.left) 
                if current.right: queue.append(current.right) 
            
            if sum > max_sum[0]: # if the max at a current level is greater than previous levels....
                max_sum = (sum, level) # set the sum and the level as the new max_sum
            level += 1 # count out them levels
            

        return max_sum[1] # return just the level     



if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(val=1, left= TreeNode(val=7, left=TreeNode(val=7), right= TreeNode(val=-8)), right= TreeNode())

    print(solution.maxLevelSum(root))