# Laboratorio 6: Problemas de Satisfacción de Restricciones (CSP)

En este laboratorio se implementa la solución de Problemas de Satisfacción de Restricciones (CSP), mediante búsqueda DFS con *backtracking* y con *forward checking*.

## Instrucciones del Proyecto

### 1. Sudoku
Implementar y comparar dos estrategias de búsqueda en profundidad (DFS) para resolver un Sudoku de $n \times n$ ($n$ debe ser un cuadrado $\ge 4$):
- **Backtracking**: retrocede cuando encuentra una incompatibilidad de restricciones.
- **Forward Checking (Filtering)**: anticipa fallos eliminando valores del dominio de variables no asignadas.

**Estructura del Árbol de Búsqueda:** En este problema, el árbol se define de la siguiente manera:
- **Estado Raíz**: El tablero inicial con las posiciones fijas.
- **Nodos**: Tableros parcialmente llenos.
- **Hijos**: El resultado de asignar un número válido (1 a 9) a la siguiente celda vacía.
- **Hojas**: Un tablero completo (solución) o un tablero donde no hay valores legales para una celda (poda).

**Especificaciones**: Deberán implementar la clase `SudokuSolver`. El usuario definirá el tamaño $n$ y el tablero inicial. **Requerimientos de la clase**:
- `__init__(self, n, board)`: Inicializa el tamaño y el estado del tablero.
- `is_valid(self, row, col, num)`: Verifica si un número puede ir en esa posición.
- `solve_backtracking()`: Implementación de DFS pura con backtracking.
- `solve_filtering()`: Implementación de DFS con Forward Checking.
- `display()`: Imprime el tablero de forma legible.

### 2. Casos de Prueba - Sudoku
Resolver un tablero de Sudoku de su elección, mediante *backtracking* y mediante *forward checking*, para los siguientes casos:
- un sudoku de $4 \times 4$
- un sudoku de $9 \times 9$ nivel fácil
- un sudoku de $9 \times 9$ nivel extremo
- un sudoku de $16 \times 16$

Para cada caso, mostrar la solución encontrada por cada método, así como el número de nodos visitados y el tiempo de ejecución de cada algoritmo. Comparar a partir de estos escenarios cuál es más eficiente.

### 3. N Queens
Colocar $N$ reinas en un tablero de ajedrez de $N \times N$ de tal manera que ninguna reina amenace a otra. Para ello, usaremos una representación de tipo permutaciones (un arreglo unidimensional de tamaño $N$, donde el índice es la fila y el valor `a[i]` es la columna).

De nuevo, deberá implementar y comparar dos estrategias de búsqueda en profundidad (DFS) para resolver el problema de $N$ reinas.

**Especificaciones**: Deberán implementar la clase `NQueensSolver`, el cual devuelve una solución para el problema de $N$ Reinas. El usuario definirá el tamaño $N$ y el tablero inicial se asume vacío.

**Requerimientos de la clase**:
- `__init__(self, n)`: Inicializa el tamaño y el estado del tablero.
- `is_valid(self, row, col)`: Verifica si hay ataques de otras piezas en el tablero a esta casilla.
- `solve_backtracking()`: Implementación de DFS pura con backtracking.
- `solve_filtering()`: Implementación de DFS con Forward Checking.
- `display()`: Imprime el tablero de forma legible.

### 4. Casos de Prueba - N Queens
Resolver un problema de $N$ reinas, mediante *backtracking* y mediante *forward checking*, para los siguientes casos:
- $N = 4$
- $N = 8$
- $N = 12$
- $N = 15$

Para cada caso, mostrar la solución encontrada por cada método, así como el número de nodos visitados y el tiempo de ejecución de cada algoritmo. Comparar a partir de estos escenarios cuál es más eficiente.

### 5. Modificación a N Queens (Todas las Soluciones)
Modificar alguno de los algoritmos para obtener **TODAS** las soluciones de un problema de $N$ reinas, y usarlo para resolver los casos:
- $N = 4$
- $N = 5$
- $N = 6$
¿Cuántas soluciones posibles hay en cada caso?

## Cómo Ejecutar

Para ejecutar los programas, asegúrate de tener Python instalado y simplemente corre en tu terminal el archivo correspondiente:

```bash
# Para ejecutar la solución de N-Reinas
python nqueens.py

# Para ejecutar la solución de Sudoku
python sudoku.py
```
