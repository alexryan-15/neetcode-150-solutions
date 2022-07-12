# A stack is used to track if the parentheses is in a valid order. If a character
# in the input a key, and the last symbol in the stack is the value, then we pop from
# the stack. If the last item is not the correct value, then the order is not valid.
# If the character is not in the stack, then we append it to the stack. If the stack
# is empty at the end, then the order is valid.
class Solution:
    def isValid(self, s: str) -> bool:
    	m = {")":"(", "]":"[", "}":"{"}
    	stack = []

    	for c in s:
    		if c in m:
				if stack and stack[-1] == m[c]:
					stack.pop()
				else:
					return False
			else:
				stack.append(c)

		return True if not stack else False
