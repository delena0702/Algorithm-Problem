# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self._diameterOfBinaryTree(root)[1]

    def _diameterOfBinaryTree(self, root: TreeNode):
        if root == None:
            return (-1, 0)
        
        left_data = self._diameterOfBinaryTree(root.left)
        right_data = self._diameterOfBinaryTree(root.right)
        return (max(left_data[0], right_data[0]) + 1, max(left_data[1], right_data[1], left_data[0] + right_data[0] + 2))
