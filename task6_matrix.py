import numpy

matrix_A = numpy.matrix('1 2 3; 4 5 6')
matrix_B = numpy.matrix('7 8; 9 1; 2 3')

def matrix_product(matrix_A, matrix_B):
	try:
		result_matrix = matrix_A.dot(matrix_B)
		print(result_matrix)
	except:
		print("error, check input data")

matrix_product(matrix_A, matrix_B)