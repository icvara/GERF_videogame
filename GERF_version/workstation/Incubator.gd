extends Workstation

var x = 1
var styleBox



func Use(player):
	if player.inventory and added_item == null:
		if player.inventory.item_ID == "Cell":
				$Timer.start()
				x=1
				$ProgressBar.show()
				added_item = player.inventory
				player.inventory.Drop(player)
				added_item.position = position + Vector2(0,0)
				$AnimatedSprite2D.show()
				$AnimatedSprite2D.play("default")

	
	elif player.inventory == null and task_finshed:
		if added_item:
			added_item.PickUP(player)
			added_item = null
			task_finshed = false
			$AnimatedSprite2D.hide()
			$ProgressBar.value = 0
			$Timer.stop()
			$ProgressBar.hide()
			$ProgressBar.modulate = Color(1,1,1)



func _on_timer_timeout() -> void:
	$ProgressBar.value += 1
	if $ProgressBar.value == 20:
		task_finshed = true
		#$Timer.stop()
		#$ProgressBar.hide()
		#$ProgressBar.value = 0
		added_item.get_node("ColorRect").color = Color(0,1,0)
		added_item.item_ID = "Bioproduct"
		x -= 0.03
		$ProgressBar.modulate = Color(1,x,x)
		
		if x <= 0:
			displaytext("Overgrown!")
			$ProgressBar.hide()
			added_item.queue_free()
			$ProgressBar.value = 0
			$ProgressBar.modulate = Color(1,1,1)
			$Timer.stop()

		
	
