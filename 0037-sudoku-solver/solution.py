from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> bool:
        # Helper functions
        def isValid(row: int, col: int, c: str) -> bool:
            return c not in rows[row] and c not in cols[col] and c not in boxes[3 * (row // 3) + (col // 3)]

        def placeNumber(row: int, col: int, c: str):
            board[row][col] = c
            rows[row].add(c)
            cols[col].add(c)
            boxes[3 * (row // 3) + (col // 3)].add(c)

        def removeNumber(row: int, col: int, c: str):
            board[row][col] = "."
            rows[row].remove(c)
            cols[col].remove(c)
            boxes[3 * (row // 3) + (col // 3)].remove(c)

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            for c in "123456789":
                if isValid(row, col, c):
                    placeNumber(row, col, c)
                    if backtrack(index + 1):
                        return True
                    removeNumber(row, col, c)
            return False

        # Precompute sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    placeNumber(r, c, board[r][c])

        # Sort empty cells by the number of possible values (constraint propagation)
        empty_cells.sort(key=lambda cell: sum(1 for c in "123456789" if isValid(cell[0], cell[1], c)))

        backtrack(0)
