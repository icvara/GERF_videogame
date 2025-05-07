extends Workstation

func Use(player):
	if player.inventory and added_item == null:
				added_item = player.inventory
				player.inventory.Drop(player)
				added_item.position = position + Vector2(0,0)
	
	elif player.inventory == null:
		if added_item:
			added_item.PickUP(player)
			added_item = null


	
