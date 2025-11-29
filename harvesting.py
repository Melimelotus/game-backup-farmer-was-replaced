# Module for harvesting-related functions
import movements

def harvest_whole_grid():
	movements.go_to([0,0])

	entities_to_ignore=[
		None,
		Entities.Grass,
		Entities.Dead_Pumpkin,
	]
	
	# First harvesting pass
	has_looped=False
	cases_to_revisit=[]
	while not has_looped:
		if can_harvest():
			harvest()
		elif not get_entity_type() in entities_to_ignore:
			# Entitity is not fully grown. Prepare next harvesting pass
			use_item(Items.Water)
			cases_to_revisit.append([get_pos_x(), get_pos_y()])
		
		movements.follow_grid()
		# Update exist conditions
		if get_pos_x()==0 and get_pos_y()==0:
			has_looped=True
	#

	# Additional harvesting passes
	farm_is_clear=False
	while not farm_is_clear:
		cases_to_revisit_on_next_pass=[]
		for case_coords in cases_to_revisit:
			# Go to target
			movements.go_to(case_coords)

			# Try to harvest or add to next harvesting pass
			if can_harvest():
				harvest()
			elif not get_entity_type() in entities_to_ignore:
				# Entitity is not fully grown. Prepare iteration
				use_item(Items.Water)
				cases_to_revisit_on_next_pass.append(case_coords)
		
		if not cases_to_revisit_on_next_pass:
			farm_is_clear=True
		else:
			case_coords=[]
			for next_coords in cases_to_revisit_on_next_pass:
				case_coords.append(next_coords)
		#
	#
	return
#