# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sametree(self,tree1,tree2):
        # both trees null
        if not tree1 and not tree2:
            return True
        #one reaches null, other still has child
        if not tree1 or not tree2:
            return False
        #both trees with diff root values
        if tree1.val!= tree2.val:
            return False
        #if above didnt return False, it means root matches, now both left & right subtrees should be same
        return self.sametree(tree1.left,tree2.left) and self.sametree(tree1.right, tree2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Base Cases
        #If root and subroot both are empty, subroot is subset of root
        if not root and not subRoot:
            return True
        # if root tree is empty and subroot is not empty, obviously not a subset
        if not root and subRoot:
            return False
        #if root not empty, subroot empty, null is always a subset of main tree
        if root and not subRoot:
            return True
        #Now check if subtree at roots are same - using helper function
        if self.sametree(root,subRoot):
            return True
        else:
            #if roots didnt match, check if subtree from left child matches or subtree from right child matches. If either of them matches, we call subset found
            #recursion of this function
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                
        