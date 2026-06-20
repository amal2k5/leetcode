# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):

        preorder = []

        def traversal(current):

            if current is None:
                return 

            preorder.append(current.val)
            traversal(current.left)
            traversal(current.right)

        traversal(root)
        return preorder        
