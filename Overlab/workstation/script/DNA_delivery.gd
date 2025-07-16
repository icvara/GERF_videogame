extends Workstation



# input_output = ["DNA","transformed_cell","bioproduct","finished"]
# color_debug = [Color(0,0,0),Color(1,0,0),Color(0,1,0),Color(1,1,1)]

func Use(player):
	if player.inventory == null:
		var new_item = item.instantiate()
		#new_item.item_ID = "Cell"
		get_parent().get_parent().add_child(new_item)
		new_item.PickUP(player)

	else:
		player.displaymsg("Hands full")
		
		



		
		
	
