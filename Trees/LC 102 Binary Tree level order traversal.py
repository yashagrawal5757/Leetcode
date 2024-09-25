# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS iterative way
        #Base case
        if root is None:
            return None
        result = []
        queue = [root]
        while queue:
            subresult = []
            for n in range(len(queue)):
                popped = queue.pop(0)
                subresult.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            result.append(subresult)
        
        return result
                


        