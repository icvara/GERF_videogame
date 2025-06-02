extends Workstation

var item_list = []
var number_item = 0

func Use(player):
	print(item_list)
	if player.inventory and number_item < 2:
		if player.inventory.item_ID == "DNA" and item_list.has("DNA") == false:
				#$Timer.start()
				#$ProgressBar.show()
				added_item = player.inventory
				item_list.append(player.inventory.item_ID )
				add_in_queue(player.inventory.item_ID )
				player.inventory.Transfer(player)
	
				number_item += 1
		elif player.inventory.item_ID == "Cell" and item_list.has("Cell") == false:
				#$Timer.start()
				#$ProgressBar.show()
				added_item = player.inventory
				item_list.append(player.inventory.item_ID )
				add_in_queue(player.inventory.item_ID )
				player.inventory.Transfer(player)
		
				number_item += 1
	elif player.inventory == null and number_item == 2:
		$Timer.start()
		$ProgressBar.show()
	
	
	elif player.inventory == null and task_finshed:
		if added_item:
			added_item.PickUP(player)
			added_item = null
			task_finshed = false

func add_in_queue(item_ID):
	$Panel.show()
	$Panel.get_node(item_ID).show()
	$Panel.get_node(item_ID).position + Vector2(0,32*number_item)

func queue_finish():
	#$Panel.show()
	for i in item_list:
		$Panel.get_node(i).hide()
	$Panel.get_node("mCell").show()
	item_list = []
func _on_timer_timeout() -> void:
	$ProgressBar.value += 1
	if $ProgressBar.value == 10:
		task_finshed = true
		$Timer.stop()
		$ProgressBar.hide()
		$ProgressBar.value = 0
		if randi_range(0,2) == 1:
			#added_item.get_node("ColorRect").color = Color(1,0,0)
			#added_item.item_ID = "Cell"
			queue_finish()
			displaytext("Success!")
		else:
			displaytext("Fail!")
			added_item.queue_free()
		
		
	
