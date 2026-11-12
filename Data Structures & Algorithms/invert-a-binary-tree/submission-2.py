# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # every time we visit a node, swap its children recusively

        # base case
        if not root:
            return None

        # do switching
        tmp = root.right
        root.right = root.left
        root.left = tmp

        # recursive on subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



        