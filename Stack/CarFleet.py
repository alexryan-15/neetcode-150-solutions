# This solution first creates pairs of the position and speed for each car to determine the number
# of car fleets. It then starts from the car that is closest to the target and works backwards. When there
# are multiple cars on the stack, if the speed of the second car is faster than that of the first, the first car
# is removed, since the second would be bottlenecked into going the speed of the car in front of it. The
# length of the stack at the end would be the number of car fleets.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    	pairs = [[p, s] for p, s in zip(position, speed)]
    	stack = []

    	for p, s in sorted(pairs)[::-1]:
    		stack.append((target - p) / s)
			if len(stack) >= 2 and stack[-1] <= stack[-2]:
				stack.pop()
		return len(stack)
