# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''DFS Recursive way
        if root is None:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''

        #bfs iterative

        #empty tree
        if root is None:
            return 0
        queue =  [root]
        levels = 0
        while(queue):
            for n in range(len(queue)):
                popped = queue.pop(0)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            levels += 1
            
        return levels

        