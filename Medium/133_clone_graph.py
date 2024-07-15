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
    
        # assuming we get a starting node
        Hashmap = {}
        queue = []
        deep_copy = Node(node.val)
        queue.append(node)

        while len(queue) > 0:
            temp = queue.pop(0)

            if temp not in Hashmap:
                for x in temp.neighbors:
                    queue.append(x)
                    deep_copy.neighbors.append(x)
                Hashmap[temp] = ""

            deep_copy = Node(temp.val)
            
        return deep_copy
            


