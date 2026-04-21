import time

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.nodes_visited = 0

    def is_valid(self, row, col):
        # Revisa si la reina en (row, col) es atacada por alguna anterior
        for r in range(row):
            c = self.board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve_backtracking(self, row=0):
        self.nodes_visited += 1

        if row == self.n:
            return True

        for col in range(self.n):
            if self.is_valid(row, col):
                self.board[row] = col
                if self.solve_backtracking(row + 1):
                    return True
                self.board[row] = -1

        return False

    def solve_filtering(self, row=0, available_cols=None):
        self.nodes_visited += 1

        if available_cols is None:
            available_cols = list(range(self.n))

        if row == self.n:
            return True

        for col in available_cols:
            if self.is_valid(row, col):
                self.board[row] = col

                # Quitar la columna usada (no puede repetirse)
                new_available = [c for c in available_cols if c != col]

                # Forward checking: verificar que la siguiente fila tenga al menos una opción válida
                if row + 1 < self.n:
                    next_valid = [c for c in new_available if self.is_valid(row + 1, c)]
                    if len(next_valid) == 0:
                        self.board[row] = -1
                        continue  # podar: la siguiente fila quedaría sin opciones

                if self.solve_filtering(row + 1, new_available):
                    return True

                self.board[row] = -1

        return False

    def display(self):
        for r in range(self.n):
            row_str = ""
            for c in range(self.n):
                if self.board[r] == c:
                    row_str += " Q "
                else:
                    row_str += " . "
            print(row_str)
        print()


def run_queens(n, use_filtering=False):
    solver = NQueensSolver(n)
    label = "Forward Checking" if use_filtering else "Backtracking"
    print(f"=== N-REINAS N={n} - {label} ===")
    start = time.time()
    if use_filtering:
        result = solver.solve_filtering()
    else:
        result = solver.solve_backtracking()
    end = time.time()

    if result:
        solver.display()
    else:
        print("No se encontró solución.\n")

    print(f"Nodos visitados: {solver.nodes_visited}")
    print(f"Tiempo: {end - start:.6f} segundos\n")


# Casos pedidos: N = 4, 8, 12, 15
for n in [4, 8, 12, 15]:
    run_queens(n, use_filtering=False)
    run_queens(n, use_filtering=True)


# =====================
# TODAS LAS SOLUCIONES (N=4,5,6)
# =====================
def find_all_solutions(n, row=0, board=None, solutions=None):
    if board is None:
        board = [-1] * n
        solutions = []

    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        valid = True
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                valid = False
                break
        if valid:
            board[row] = col
            find_all_solutions(n, row + 1, board, solutions)
            board[row] = -1

    return solutions


print("=" * 40)
print("TODAS LAS SOLUCIONES DE N-REINAS")
print("=" * 40)
for n in [4, 5, 6]:
    solutions = find_all_solutions(n)
    print(f"N={n}: {len(solutions)} soluciones posibles")
    print(f"  Primera solución: {solutions[0]}\n")