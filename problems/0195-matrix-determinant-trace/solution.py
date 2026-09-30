def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	trace = 0
	for i in range(len(matrix)):
		j = i
		trace += matrix[i][j]
	def dete(matrix):
		if len(matrix[0]) == 2:
			return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
		det = 0
		for col in range(len(matrix)):
			minor = [[matrix[i][j] for j in range(len(matrix)) if j != col] for i in range(1, len(matrix))]
			det += (((-1)**col)*(matrix[0][col]*dete(minor)))
		return det
	return (dete(matrix), trace)