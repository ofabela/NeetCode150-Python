from collections import deque
class Solution:
	#Recursive DFS 
	def maxDepth(self, root: TreeNode) -> TreeNode:
		if not root:
			return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	#Itartive DFS
	def maxDepthBFS(self, root: TreeNode) -> TreeNode:
		stack = [[root, 1]]
		res = 0 

		while stack:
			node, depth = stack.pop()

			if node:
				res = max(res, depth)
				stack.append([node.left, depth+1])
				stack.append([node.right, depth+1])
		return res


	#Iterative BFS 
	def maxDepthDFS(self, root: TreeNode) -> TreeNode:
		if not root:
			return 0
		depth = 0
		q = deque([root])

		while q:
			for i in range(len(q)):
				node = q.poplef()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			depth += 1
		return depth
			

		