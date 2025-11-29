# Module for maze creation and exploration
import planting
import movements

def create_maze():
	# Plant bush and apply substance
	movements.go_to([0,0])
	planting.plant_on_desired_soil(Entities.Bush)
	amount_to_use=get_world_size() * 2**(num_unlocked(Unlocks.Mazes)-1)
	use_item(Items.Weird_Substance, amount_to_use)
	return

def traverse_maze(forward_index):
	# Traverse maze while keeping a wall to the drone's right
	directions_dict={
		0:North,
		1:East,
		2:South,
		3:West
	}
	rightward_index=(forward_index+1)%4
	rightward_direction=directions_dict[rightward_index]

	if can_move(rightward_direction):
		# No wall on the right, move there
		move(rightward_direction)
		return rightward_index
	
	forward_direction=directions_dict[forward_index]
	if can_move(forward_direction):
		# Wall on the right, press forward
		move(forward_direction)
		return forward_index
	
	leftward_index=(forward_index+3)%4
	leftward_direction=directions_dict[leftward_index]
	if can_move(leftward_direction):
		# Wall on the right and forward, move left
		move(leftward_direction)
		return leftward_index
	
	backward_index=(forward_index+2)%4
	backward_direction=directions_dict[backward_index]
	if can_move(backward_direction):
		# Wall on the right and forward, move left
		move(backward_direction)
	return backward_index

# TODO
def map_maze():
	# Go through the whole maze once to create and return a heatmap
	all_coords=[]
	for x in range(0, get_world_size()):
		for y in range(0, get_world_size()):
			all_coords.append([x,y])
	heat_map_dict={}

	maze_is_mapped=False
	drone_direction_index=0
	while not maze_is_mapped:
		# Keep a wall to the right of the drone
		next_direction_index=traverse_maze(drone_direction_index)
		drone_direction_index=next_direction_index

		# Update exit condition
		maze_is_mapped=True
		for coords in all_coords:
			if not coords in heat_map_dict:
				maze_is_mapped=False
				break
	# ensure every case has been mapped
	# assign a value to each coordinate: value indicates distance to reference
	# point (start position of drone or treasure location once maze is reused)
	return
#