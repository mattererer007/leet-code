from typing import Optional
from collections import deque 

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.

"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# O(n) time complexity where n is the number of nodes
# O(n) space complexirty to account for the quque, visited dictionary, and copy (3N at most?)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Check if nod eis provided
        if not node:
            return None
        else:
            # Create a queu startign with provided node
            queue = deque([node])
            # dictionary to track visited items
            visited ={}

            # Clone first node to return
            clone_node = Node(val = node.val)

            # immeidately at this first node to dictionary
            visited[clone_node.val] = clone_node

            # While there are new nodes to visit...
            while queue:
                curr = queue.popleft()

                # pull copy from dict because the first node clone will already be tehre
                curr_clone = visited[curr.val]

                # Iterate and check if any neighbors ahve yet to be visited
                ## If so... add to queue for later review
                ## Create clone
                for n in curr.neighbors:
                    if n.val not in visited:
                        visited[n.val] = Node(val = n.val)
                        queue.append(n)

                    # Add clone to neighbors
                    curr_clone.neighbors.append(visited[n.val])
    
        return clone_node
    

if __name__ == "__main__":
    # Build the original graph manually
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # root node to pass to cloneGraph
    original_graph = node1

    solution = Solution()
