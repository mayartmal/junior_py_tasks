import math

input_data = [[0.3, 0.999] ,[-0.5, 0.5], [0.6, 0.6], [0.7, 0.7], [0.8, 0.8], [0.9, 0.9], [0.95, 0.9]]


def coords_checker(input_data):
	for coords in input_data:
		x_coord = abs(coords[0])
		y_coord = abs(coords[1])
		angle = math.atan(y_coord/x_coord)
		max_x_coord_value = math.cos(angle)
		max_y_coord_value = math.sin(angle)
		if (x_coord <= max_x_coord_value) & (y_coord <= max_y_coord_value):
			print("coords in circle")
		else:
			print("coords not in circle")	

coords_checker(input_data)
