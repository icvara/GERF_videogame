extends Workstation


func Use(player):
	if player.inventory and added_item == null:
		if player.inventory.item_ID == "DNA" :
				$Timer.start()
				$ProgressBar.show()
				added_item = player.inventory
				player.inventory.Drop(player)
				added_item.position = position + Vector2(0,0)
	
	elif player.inventory == null and task_finshed:
		if added_item:
			added_item.PickUP(player)
			added_item = null
			task_finshed = false

func _on_timer_timeout() -> void:
	$ProgressBar.value += 1
	if $ProgressBar.value == 10:
		task_finshed = true
		$Timer.stop()
		$ProgressBar.hide()
		$ProgressBar.value = 0
		if randi_range(0,2) == 1:
			added_item.get_node("ColorRect").color = Color(1,0,0)
			added_item.item_ID = "Cell"
			displaytext("Success!")
		else:
			displaytext("Fail!")
			added_item.queue_free()
		
		
	
