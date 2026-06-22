# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):

        postorder = []
        
        def traversal(current):
            if current is None:
                return

            traversal(current.left)
            traversal(current.right)
            postorder.append(current.val)

        traversal(root)
        return postorder    
