# Module for planting-related functions
import movements

entities_ground_type_dict={
	Entities.Bush: 'any',
	Entities.Carrot: 'soil',
	Entities.Grass: 'any',
	Entities.Pumpkin: 'soil',
	Entities.Sunflower: 'soil',
	Entities.Tree: 'any',
}

def plant_on_desired_soil(entity, use_water=False, use_fertilizer=False):
	desired_soil=entities_ground_type_dict[entity]
	# Prepare ground
	if desired_soil=='soil':
		if not get_ground_type()==Grounds.Soil:
			till()
	# Plant
	plant(entity)
	if use_water:
		use_item(Items.Water)
	if use_fertilizer:
		use_item(Items.Fertilizer)
	return

def plant_everywhere(entity, use_water=False, use_fertilizer=False):
	movements.go_to([0,0])
	has_looped=False
	while not has_looped:
		if can_harvest():
			harvest()
		plant_on_desired_soil(entity, use_water, use_fertilizer)
		movements.follow_grid()
		if get_pos_x()==0 and get_pos_y()==0:
			has_looped=True
	return

def plant_in_checker_pattern(entity, even=True, use_water=False, use_fertilizer=False):
	# Plant the entity accross the whole farm following a checkerboard pattern.
	# Checkerboard can be even (starts at 0,0) or odd (starts at 0,1)
	coordinates_list=[]
	if even:
		coordinates_list=movements.build_checker_coordinates_list()[0]
	else:
		coordinates_list=movements.build_checker_coordinates_list()[1]

	for coords in coordinates_list:
		movements.go_to(coords)
		if can_harvest():
			harvest()
		plant_on_desired_soil(entity, use_water, use_fertilizer)
	return
#