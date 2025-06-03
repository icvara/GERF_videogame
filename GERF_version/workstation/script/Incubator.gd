extends Workstation

var x = 1
var styleBox

var dead = false

func Use(player):
	if player.inventory and added_item == null:
		if player.inventory.item_ID == "mCell":
				$Timer.start()
				x=1
				$ProgressBar.show()
				added_item = player.inventory.item_ID
				player.inventory.Transfer(player)
				#added_item.position = position + Vector2(0,0)
				$mCell.show()
				$mCell.play("default")

			
	elif task_finshed:
		if player.inventory == null:
			task_finshed = false
			var new_item = item.instantiate()
			#new_item.item_ID = "Cell"
			get_parent().get_parent().add_child(new_item)
			new_item.PickUP(player)
			added_item = null
			$mCell.hide()
			$ProgressBar.value = 0
			$Timer.stop()
			$ProgressBar.hide()
			$ProgressBar.modulate = Color(1,1,1)


		else:
			player.displaymsg("hands full")

func _on_timer_timeout() -> void:
	$ProgressBar.value += 1
	if $ProgressBar.value == 20:
		task_finshed = true
		$mCell.play("prod")
		#$Timer.stop()
		#$ProgressBar.hide()
		#$ProgressBar.value = 0
		#added_item.get_node("ColorRect").color = Color(0,1,0)
		#added_item.item_ID = "Bioproduct"
		x -= 0.03
		$ProgressBar.modulate = Color(1,x,x)
		
		if x <= 0:
			displaytext("Overgrown!")
			dead = true
			task_finshed = false
			$mCell.play("fail")
			$ProgressBar.hide()
			#added_item.queue_free()
			
			$ProgressBar.value = 0
			$ProgressBar.modulate = Color(1,1,1)
			$Timer.stop()

		
	


func _on_m_cell_animation_finished() -> void:
	if dead:
		$mCell.hide()
		dead=false
		added_item = null
