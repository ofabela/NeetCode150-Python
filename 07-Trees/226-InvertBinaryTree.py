from TreeNode import TreeNode
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode :
		if root:
			self.invertTree(root.left)
			self.invertTree(root.right)

			root.left, root.right = root.right, root.left

		return root

ex = Solution()

