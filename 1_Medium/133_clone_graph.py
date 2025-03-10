"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;

## NEED TO ASK WHAT IS A DEEP COPY
## NEED TO ASK HOW VALUES ARE PROVIDED
## ALWAYS CHECK IN INPUT IS NONE
## HOW DO I CREATE A COPY
## ASK IF COMPLETE CONNECTED


}


"""
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        # Create dictionary of nodes where original node is key and new 'deep' copy is the value
        start = node # create copy as a good practice
        nodesToDict = {} # dictionary to store [node] = copy of node
        queue = [] # BFS through graph
        queue.append(start) # start

        while len(queue) > 0: # While there are nodes to explore
            current = queue.pop(0) # take off the top (FIFO)
            nodesToDict[current] = Node(val=current.val) # Create dictionary entry with duplicate (no neighbors assigned yet)
            for x in current.neighbors: # For each neighbor...
                if x not in nodesToDict: # Check if already in dictionary (O(1))
                    queue.append(x) # if not yet added...add


        # Iterate through key and find neighbors to then attach to deep copy of itself
        for key, value in nodesToDict.items(): # iterate through each nodes
            for x in key.neighbors: #grab the neighbors of original node
                neighbor_copy = nodesToDict.get(x)
                value.neighbors.append(neighbor_copy) # add copy of each neighbor node to copy of current node


        # return deep copy 
        return nodesToDict[node]
    


if __name__ == '__main__':
    
    solution = Solution()
    # build a square node
    """
    1 -- 2
    |    |
    4 -- 3
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors.append(node2)
    node2.neighbors.append(node1)
    node3.neighbors.append(node2)
    node4.neighbors.append(node1)
    node1.neighbors.append(node4)
    node2.neighbors.append(node3)
    node3.neighbors.append(node4)
    node4.neighbors.append(node2)

    node_test = solution.cloneGraph(node1)

    for x in node_test.neighbors:
        print(x.val)


