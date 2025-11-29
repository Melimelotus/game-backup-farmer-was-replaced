# Module for movement-related functions

def build_checker_coordinates_list():
	# Return two lists of coordinates. Each list corresponds to one of the two
	# colors on a checkerboard.
	max_coordinate=get_world_size()
	checker_even_coordinates_list=[]
	checker_odd_coordinates_list=[]
	for x in range(0, max_coordinate):
		x_is_even=x%2==0
		for y in range(0, max_coordinate):
			y_is_even=y%2==0
			if (y_is_even and x_is_even) or (not y_is_even and not x_is_even):
				checker_even_coordinates_list.append([x, y])
	return checker_even_coordinates_list, checker_odd_coordinates_list

def follow_grid():
	if get_pos_y()==get_world_size()-1:
		move(East)
	move(North)
	return

def go_to(coords):
	# Get information
	current_x=get_pos_x()
	current_y=get_pos_y()
	world_size=get_world_size()

	# Unpack
	target_x=coords[0]
	target_y=coords[1]

	# Calculate movement values
	distance_x=abs(target_x-current_x)
	move_eastward=target_x>current_x

	distance_y=abs(target_y-current_y)
	move_northward=target_y>current_y

	# Determine shortest path
	if abs(distance_x) > world_size/2:
		# Faster to go in the other direction. Adjust values
		distance_x=world_size % distance_x
		move_eastward=not move_eastward

	if abs(distance_y) > world_size/2:
		# Faster to go in the other direction. Adjust values
		distance_y=world_size % distance_y
		move_northward=not move_northward

	# Move
	for i in range(distance_x):
		if move_eastward:
			move(East)
		else:
			move(West)
	for i in range(distance_y):
		if move_northward:
			move(North)
		else:
			move(South)
	return
#