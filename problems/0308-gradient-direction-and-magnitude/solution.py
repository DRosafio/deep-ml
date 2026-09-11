import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient = np.array(gradient)
	if np.sum(gradient) != 0:
		mag = float(np.sqrt(np.sum(gradient ** 2)))
		direction = gradient/mag
		desc_direction = -1*direction
		return {'magnitude' : mag, 'direction' : direction, 'descent_direction' : desc_direction}
	else:
		return {'magnitude' : 0, 'direction' : [0,0], 'descent_direction' : [0,0]}
