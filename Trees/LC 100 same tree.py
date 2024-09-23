# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base case: if both p and q are None: they are still same so return True
        if p is None and  q is None:
            return True
        # if one of them is None but other isnt - return False
        if p is None or q is None:
            return False
        #if values are different -> return False
        if p.val != q.val:
            return False
        #check left subtree is same or not, check right subtree is same or not, if both sides return True then we say its identical - so AND operation
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        