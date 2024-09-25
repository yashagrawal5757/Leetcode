# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isvalid(self,node,low,high):
        #Helper funcn to check if subtree is valid or not
        #For valid - node > low and node < high
            if node is None:
                #leaf node reached
                return True
            #if condition failed, instantly return False else check both subchilds
            if node.val <= low or node.val >=high:
                return False
            return self.isvalid(node.left,low,node.val) and self.isvalid(node.right,node.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check if root is in neg inf to pos inf range or not. 
        #internatlly it checks left and right subtree are valid or not
        return self.isvalid(root, float('-inf'),float('+inf')) 
        
        