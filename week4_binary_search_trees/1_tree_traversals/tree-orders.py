# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c

	def inOrder(self):
		self.result = []

		def helper(i, res):
			if i != -1:
				helper(self.left[i], res)
				self.result.append(self.key[i])
				helper(self.right[i], res)

		helper(0, self.result)
		return self.result

	def preOrder(self):
		self.result = []

		def helper(i, res):
			if i != -1:
				self.result.append(self.key[i])
				helper(self.left[i], res)
				helper(self.right[i], res)

		helper(0, self.result)
		return self.result

	def postOrder(self):
		self.result = []

		def helper(i, res):
			if i != -1:
				helper(self.left[i], res)
				helper(self.right[i], res)
				self.result.append(self.key[i])

		helper(0, self.result)
		return self.result


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
