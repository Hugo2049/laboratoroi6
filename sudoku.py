import time

class SudokuSolver:
    def __init__(self, n, board):
        self.n = n
        self.board = [row[:] for row in board]
        self.box_size = int(n ** 0.5)
        self.nodes_visited = 0

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False
        for r in range(self.n):
            if self.board[r][col] == num:
                return False
        box_row = (row // self.box_size) * self.box_size
        box_col = (col // self.box_size) * self.box_size
        for r in range(box_row, box_row + self.box_size):
            for c in range(box_col, box_col + self.box_size):
                if self.board[r][c] == num:
                    return False
        return True

    def find_empty(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == 0:
                    return (r, c)
        return None

    def find_empty_mrv(self, domains):
        # MRV: elige la celda vacía con menos valores posibles
        best_cell = None
        min_options = float('inf')
        for (r, c), vals in domains.items():
            if self.board[r][c] == 0 and len(vals) < min_options:
                min_options = len(vals)
                best_cell = (r, c)
        return best_cell

    def solve_backtracking(self, max_nodes=500000):
        self.nodes_visited += 1
        if self.nodes_visited > max_nodes:
            return None

        empty = self.find_empty()
        if empty is None:
            return True

        row, col = empty
        for num in range(1, self.n + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                result = self.solve_backtracking(max_nodes)
                if result is True:
                    return True
                if result is None:
                    return None
                self.board[row][col] = 0
        return False

    def get_domains(self):
        domains = {}
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == 0:
                    domains[(r, c)] = [num for num in range(1, self.n + 1)
                                       if self.is_valid(r, c, num)]
        return domains

    def solve_filtering(self, domains=None):
        if domains is None:
            domains = self.get_domains()

        self.nodes_visited += 1

        empty = self.find_empty_mrv(domains)
        if empty is None:
            return True

        row, col = empty
        for num in list(domains.get((row, col), [])):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                new_domains = {}
                valid = True
                for key, vals in domains.items():
                    if key == (row, col):
                        continue
                    es_vecino = (
                        key[0] == row or
                        key[1] == col or
                        (key[0] // self.box_size == row // self.box_size and
                         key[1] // self.box_size == col // self.box_size)
                    )
                    new_vals = [v for v in vals if v != num] if es_vecino else vals[:]
                    if len(new_vals) == 0 and self.board[key[0]][key[1]] == 0:
                        valid = False
                        break
                    new_domains[key] = new_vals

                if valid and self.solve_filtering(new_domains):
                    return True

                self.board[row][col] = 0
        return False

    def display(self):
        for r in range(self.n):
            if r % self.box_size == 0 and r != 0:
                print("-" * (self.n * 3))
            row_str = ""
            for c in range(self.n):
                if c % self.box_size == 0 and c != 0:
                    row_str += " | "
                row_str += f"{self.board[r][c]:2} "
            print(row_str)
        print()


def run_case(title, solver_class, board, n, use_filtering=False, max_nodes=500000):
    solver = solver_class(n, board)
    start = time.time()
    if use_filtering:
        result = solver.solve_filtering()
        label = "Forward Checking"
    else:
        result = solver.solve_backtracking(max_nodes)
        label = "Backtracking"
    end = time.time()

    print(f"=== {title} - {label} ===")
    if result is None:
        print("Superó el límite de nodos. Demasiado lento.")
    else:
        solver.display()
    print(f"Nodos visitados: {solver.nodes_visited}")
    print(f"Tiempo: {end - start:.6f} segundos\n")


# =====================
# SUDOKU 4x4
# =====================
board_4x4 = [
    [1, 0, 0, 4],
    [0, 4, 0, 0],
    [0, 0, 3, 0],
    [3, 0, 0, 2]
]
run_case("SUDOKU 4x4", SudokuSolver, board_4x4, 4, use_filtering=False)
run_case("SUDOKU 4x4", SudokuSolver, board_4x4, 4, use_filtering=True)


# =====================
# SUDOKU 9x9 - FÁCIL
# =====================
board_9x9_easy = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
run_case("SUDOKU 9x9 FÁCIL", SudokuSolver, board_9x9_easy, 9, use_filtering=False)
run_case("SUDOKU 9x9 FÁCIL", SudokuSolver, board_9x9_easy, 9, use_filtering=True)


# =====================
# SUDOKU 9x9 - EXTREMO
# =====================
board_9x9_extreme = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
run_case("SUDOKU 9x9 EXTREMO", SudokuSolver, board_9x9_extreme, 9, use_filtering=False)
run_case("SUDOKU 9x9 EXTREMO", SudokuSolver, board_9x9_extreme, 9, use_filtering=True)


# =====================
# SUDOKU 16x16
# (tablero con suficientes pistas para resolverse en segundos)
# =====================
board_16x16 = [
    [ 0,  2,  0,  4,  0,  6,  0,  8,  0, 10,  0, 12,  0, 14,  0, 16],
    [ 5,  6,  7,  8,  1,  2,  3,  4, 13, 14, 15, 16,  9, 10, 11, 12],
    [ 0, 10,  0, 12,  0, 14,  0, 16,  0,  2,  0,  4,  0,  6,  0,  8],
    [13, 14, 15, 16,  9, 10, 11, 12,  5,  6,  7,  8,  1,  2,  3,  4],
    [ 0,  1,  0,  3,  0,  5,  0,  7,  0,  9,  0, 11,  0, 13,  0, 15],
    [ 6,  5,  8,  7,  2,  1,  4,  3, 14, 13, 16, 15, 10,  9, 12, 11],
    [ 0,  9,  0, 11,  0, 13,  0, 15,  0,  1,  0,  3,  0,  5,  0,  7],
    [14, 13, 16, 15, 10,  9, 12, 11,  6,  5,  8,  7,  2,  1,  4,  3],
    [ 0,  4,  0,  2,  0,  8,  0,  6,  0, 12,  0, 10,  0, 16,  0, 14],
    [ 7,  8,  5,  6,  3,  4,  1,  2, 15, 16, 13, 14, 11, 12,  9, 10],
    [ 0, 12,  0, 10,  0, 16,  0, 14,  0,  4,  0,  2,  0,  8,  0,  6],
    [15, 16, 13, 14, 11, 12,  9, 10,  7,  8,  5,  6,  3,  4,  1,  2],
    [ 0,  3,  0,  1,  0,  7,  0,  5,  0, 11,  0,  9,  0, 15,  0, 13],
    [ 8,  7,  6,  5,  4,  3,  2,  1, 16, 15, 14, 13, 12, 11, 10,  9],
    [ 0, 11,  0,  9,  0, 15,  0, 13,  0,  3,  0,  1,  0,  7,  0,  5],
    [16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1],
]

run_case("SUDOKU 16x16", SudokuSolver, board_16x16, 16, use_filtering=False)
run_case("SUDOKU 16x16", SudokuSolver, board_16x16, 16, use_filtering=True)