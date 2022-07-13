# This solution uses a stack and recursion to generate all of the combinations of parentheses
# for a given number. If there is an even number of open and closed symbols generated,
# and that number is equal to n, then the solution is added to the results. If not, it
# does some recursion to generate other solutions.
class Solution:
	def generateParentheses(self, n: int) -> List[str]:
		stack = []
		res = []

		def backtrack(op, cl):
			if op == cl == n:
				res.append("".join(stack))
				return

			if op < n:
				stack.append("(")
				backtrack(op + 1, cl)
				stack.pop()
			if cl < op:
				stack.append(")")
				backtrack(op, cl + 1)
				stack.pop()

		backtrack(0,0)
		return res
