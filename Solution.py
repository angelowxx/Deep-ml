from __future__ import annotations

import math

import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	determint = trace*trace - 4*det
	if determint < 0:
		return []
	eigen_value = (trace+math.sqrt(determint))/2
	eigenvalues = [eigen_value]
	if determint > 0:
		eigen_value1 = (trace-math.sqrt(determint))/2
		eigenvalues.append(eigen_value1)

	return eigenvalues

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = matrix.copy()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[i][j] = result[i][j] * scalar
	return result

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode.__eq__("row"):
		means = calculate_matrix_mean_row(matrix)
	elif mode.__eq__("column"):
		means = calculate_matrix_mean_column(matrix)
	return means


def calculate_matrix_mean_column(matrix: list[list[float]]) -> list[float]:
	means = [0 for i in range(len(matrix[0]))]
	for i in range(len(matrix[0])):
		tmp = 0
		for j in range(len(matrix)):
			tmp += matrix[j][i]
		means[i] = tmp / len(matrix)
	return means


def calculate_matrix_mean_row(matrix: list[list[float]]) -> list[float]:
	means = [0 for i in range(len(matrix))]
	for i in range(len(matrix)):
		tmp = 0
		for j in range(len(matrix[0])):
			tmp += matrix[i][j]
		means[i] = tmp / len(matrix[0])
	return means


def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
	# Write your code here and return a python list after reshaping by using numpy's tolist() method
	reshaped_matrix = np.reshape(a, new_shape).tolist()
	return reshaped_matrix

if __name__ == '__main__':
    reshape_matrix()