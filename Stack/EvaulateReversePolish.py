# This solution uses a stack to calculate the expression in the proper order. An item is
# appended to the stack when an operator is found in the expression. The operation is done
# on the two items on the top of the stack, and then the new item is appended. Any integer
# is just appended to the stack directly. There will be one item left on the stack at the
# end of evaluation, which is the answer.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    	stack = []
    	for c in tokens:
    		if c == "+":
    			stack.append(stack.pop() + stack.pop())
			elif c = "-"
				a, b = stack.pop(), stack.pop()
				stack.append(b - a)
			elif c = "*"
				stack.append(stack.pop() * stack.pop())
			elif c = "/"
				a, b = stack.pop(), stack.pop()
				stack.append(int(b / a))
			else:
				stack.append(int(c))
		return stack[0]
