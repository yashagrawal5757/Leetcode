"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node,map):
        #get the clone of current node from map
        node_clone = map[node]
        
        for neighbor in node.neighbors: #find neighbors from original node
            if neighbor in map:  #if clone already present, just make the connection in clone 
                node_clone.neighbors.append(map[neighbor])  #Important (Draw and see)
            else:
                #neighbor not cloned yet, so make a clone of neighbor node, add it to map
                neighbor_clone = Node(neighbor.val)
                map[neighbor] = neighbor_clone
                #Make connection of original cloned node to new neighbor clone
                node_clone.neighbors.append(neighbor_clone)
                self.dfs(neighbor,map)
        #when no more neighbors left, backtrack by returning False
        return False

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: #edge case where node is empty
            return None

        map = {}
        #clone the  root node
        node_clone = Node(node.val)
        #add node:clonednode to map 
        map[node] = node_clone

        #dfs at current node
        self.dfs(node,map)
        #when all nodes traversed, control comes here
        return node_clone
        #we are able to return node_clone because in Python objects of custom class are mutable
        #node_clone is object of class Node, hence it is mutable. So it is populated inside dfs and returned in cloneGraph method
        
        