# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Base cases
        #Leaf node found - return None
        if root is None:
            return None
        #Root node has either of p or q - root node becomes LCA
        if root == p:
            return p
        if root ==q:
            return q
        #root node is not p/q, go to left side. check each if p or q found, return that
        left = self.lowestCommonAncestor(root.left,p,q)
        right= self.lowestCommonAncestor(root.right,p,q)
        #if one of them is none, it means they are on same side. whichever was above level is LCA
        if not left:
            return right
        if not right:
            return left
        #if both left & right are not None, it means p,q found on either sides - root was LCA.        
        return root
        