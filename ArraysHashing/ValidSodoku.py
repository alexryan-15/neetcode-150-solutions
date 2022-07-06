# This solution uses dictionaries for the rows, columns, and squares to track the numbers on the sudoku board
# If a number has already appeared in the same row, column, or square, the board is not valid. After every number
# is iterated through, it is added to each of the dictionaries for the current row, col, and square.
class Solution:
	def isValidSodoku(self, board: List[List[str]]) -> bool:
		cols = collections.defaultdict(set)
		rows = collections.defaultdict(set)
		squares = collections.defaultdict(set)

		for r in range(9):
			for c in range(9):
				if board[r][c] == ".":
					continue
				if (board[r][c] in rows[r] or
					board[r][c] in cols[c] or
					board[r][c] in squares[(r // 3, c // 3)]
					return False
				cols[c].add(board[r][c])
				rows[r].add(board[r][c])
				squares[(r // 3, c // 3)].add(board[r][c])

		return True
