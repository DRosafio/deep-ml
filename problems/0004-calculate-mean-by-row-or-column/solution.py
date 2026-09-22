def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for i in matrix:
			means.append(sum(i)/len(i))
	if mode == 'column':
		for j in range(len(matrix[0])):
			mean = 0
			t = 0
			for i in range(len(matrix)):
				mean += matrix[i][j]
				t += 1
			means.append(mean/t)
	return means