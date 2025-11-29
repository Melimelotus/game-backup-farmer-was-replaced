# Main script
import mazework
import movements
import planting

# TODO switch for polyculture
def plant_for_wood(trees_only=False):
	x_is_even=get_pos_x()%2==0
	y_is_even=get_pos_y()%2==0
	if (y_is_even and x_is_even) or (not y_is_even and not x_is_even):
		plant(Entities.Tree)
	else:
		if trees_only:
			return
		plant(Entities.Bush)
	return

# TODO refactor
def farm_for_weird_substance():
	# Best yield: trees
	# TODO: remove harvested trees from polyculture conflicts list
	# TODO: check if desired companion is already planted
	# Prepare weird substance season
	movements.go_to([0,0])
	change_hat(Hats.Wizard_Hat)
	checker_even_coordinates_list, checker_odd_coordinates_list=movements.build_checker_coordinates_list()

	# Plant and fertilize trees
	index=0
	trees_dict={}
	polyculture_wishes_dict={}
	for tree_coordinates in checker_even_coordinates_list:
		movements.go_to(tree_coordinates)
		if can_harvest():
			harvest()
		plant(Entities.Tree)
		use_item(Items.Fertilizer)
		trees_dict[index]=tree_coordinates

		# Prepare polyculture
		polyculture_wish=get_companion()
		if polyculture_wish:
			# Sometimes get_companion returns None
			polyculture_wishes_dict[index]=polyculture_wish

		index+=1

	# Harvest
	for index in trees_dict:
		# Unpack data
		tree_coordinates=trees_dict[index]
		polyculture_wish=polyculture_wishes_dict[index]
		polyculture_coords=list(polyculture_wish[1])

		can_do_polyculture=not polyculture_coords in checker_even_coordinates_list

		if can_do_polyculture:
			movements.go_to(polyculture_coords)
			polyculture_companion=polyculture_wish[0]
			planting.plant_on_desired_soil(polyculture_companion)

		movements.go_to(tree_coordinates)
		if can_harvest():
			harvest()

	# Harvest leftovers
	movements.go_to([0,0])
	looped=False
	while not looped:
		if can_harvest():
			harvest()
		movements.follow_grid()
		if get_pos_x()==0 and get_pos_y()==0:
			looped=True
	return

# General conditions
cultivate_weird_substance=False
do_mazework=True
do_work=True

while do_work==True:
	# MAZES
	if do_mazework:
		# harvesting.harvest_whole_grid()
		# mazework.create_maze()
		mazework.map_maze()
		do_work=False
		continue
	
	# WEIRD SUBSTANCE
	if cultivate_weird_substance:
		# Farm for weird substance if enough fertilizer on hand
		fertilizer_amount_required=get_world_size()**2/2
		if num_items(Items.Fertilizer) > fertilizer_amount_required:
			farm_for_weird_substance()

	# GENERIC FARMING
	# Harvest
	if can_harvest():
		harvest()

	# Plant according to needs
	if num_items(Items.Hay) < num_items(Items.Wood)*1.2:
		# Hay needed
		plant(Entities.Grass)
	elif num_items(Items.Wood) < num_items(Items.Carrot)*1.5:
		# Wood needed
		plant_for_wood()
	elif num_items(Items.Carrot) < num_items(Items.Pumpkin)*1.5:
		# Carrots needed
		planting.plant_on_desired_soil(Entities.Carrot)
	else:
		# Pumpkins needed
		#enter_pumpkin_season()
		planting.plant_on_desired_soil(Entities.Pumpkin)

	# Move
	movements.follow_grid()
#