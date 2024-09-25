# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, li):
        if root is None:
            return None
        self.inorder(root.left,li)
        li.append(root)
        self.inorder(root.right,li)
        return li

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        li =  self.inorder(root, li)
        print(li[k-1])
        return li[k-1]
        