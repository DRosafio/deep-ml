def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	new_mat = []
	for i in range(len(matrix)):
		new_row = []
		for j in range(len(matrix[0])):
			new_row.append(scalar * matrix[i][j])
		new_mat.append(new_row)
	return new_mat