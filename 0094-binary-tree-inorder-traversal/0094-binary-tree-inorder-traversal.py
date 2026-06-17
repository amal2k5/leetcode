# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):

        result = []

        def traversal(current):

            if current is None:
                return

            traversal(current.left)
            result.append(current.val)
            traversal(current.right)

        traversal(root)
        return result    



        