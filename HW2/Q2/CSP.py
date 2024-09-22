import random
import sys

import numpy as np

sys.setrecursionlimit(100000)
class CSP:
    def __init__(self, n):
        self.variables = [-1] * n
        self.n = n
        self.grid = np.array(np.zeros(shape=(n, n), dtype=int))
        self.domain = np.array(np.ones(shape=(n, n), dtype=int))
        self.number_of_iteration = 0
        self.first = 0

    def check_constraints(self) -> bool:
        res = True
        for row in range(0, self.n):
            for col in range(self.first - 1, self.n):
                res = res and not self.is_attack(row, col)
                if self.is_attack(row, col):
                    self.domain[row][col] = 0
        return res

    def is_attack(self, row, col):
        N = self.n
        for k in range(0, N):
            if self.grid[row][k] == 1 or self.grid[k][col] == 1:
                return True

        for k in range(0, N):
            for l in range(0, N):
                if (k + l == row + col) or (k - l == row - col):
                    if self.grid[k][l] == 1:
                        return True
        return False

    def is_safe(self, row, col):
        for i in range(col):
            if self.grid[row][i] == 1:
                return False

        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.grid[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.grid[i][j] == 1:
                return False

        return True

    def assign(self, row, column):
        self.grid[row][column] = 1

    def _solve_problem_with_backtrack(self, i):
        self.number_of_iteration += 1
        N = self.n
        if i >= N:
            return True

        for j in range(N):
            if self.is_safe(j, i):
                self.grid[j][i] = 1
                if self._solve_problem_with_backtrack(i + 1):
                    return True
                self.grid[j][i] = 0
        return False

    def solve_problem_with_backtrack(self):
        self._solve_problem_with_backtrack(0)
        return self.grid

    def forward_check(self, i):
        self.check_constraints()
        for k in range(self.variables[i] + 1, self.n):
            if self.domain[k][i] == 1:
                self.variables[i] = k
                return True
        self.variables[i] = -1
        return False

    def _solve_problem_with_forward_check(self, i):
        self.number_of_iteration += 1
        if i == self.n:
            return True
        if i == 0:
            self.variables[0] += 1
            self.assign(self.variables[0], 0)
            self._solve_problem_with_forward_check(1)
        else:
            if self.forward_check(i):
                self.assign(self.variables[i], i)
                self._solve_problem_with_forward_check(i + 1)
            else:
                coordinates = (self.variables[i - 1], i - 1)
                self.grid[coordinates[0]][coordinates[1]] = 0
                n = self.n
                self.first = i
                self.domain = np.array(np.ones(shape=(n, n), dtype=int))
                self._solve_problem_with_forward_check(i - 1)
        return True

    def solve_problem_with_forward_check(self):
        if self._solve_problem_with_forward_check(0):
            return self.grid
        else:
            n = self.n
            return np.array(np.zeros(shape=(n, n), dtype=int))
