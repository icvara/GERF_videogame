extends Workstation

func Use(player):
	if player.inventory and added_item == null:
				added_item = player.inventory
				#player.inventory.Drop(player)
				

				player.inventory = null
				added_item.player_holding = null
	
	
				added_item.freeze_mode = 0
				added_item.linear_velocity = Vector2(0,0)
				added_item.set_collision_layer_value(1,false)
				added_item.set_collision_mask_value(1,false)
				await get_tree().create_timer(0.01).timeout
				z_index = 1
				added_item.global_position = global_position + Vector2(32,32)
				#print(added_item.position)

	
	
	elif player.inventory == null:
		if added_item:
			added_item.PickUP(player)
			added_item = null
