extends StaticBody2D


@export var ID = 0

var action_time = 1.0
var added_item
var task_finshed = false

var input_output = ["DNA","transformed_cell","bioproduct","finished"]
var color_debug = [Color(0,0,0),Color(1,0,0),Color(0,1,0),Color(1,1,1)]

func Use(player):
	if player.inventory:
		if player.inventory.item_ID == input_output[ID]:
			if ID == 2:
				player.inventory.queue_free()
				GlobalVariableOverlab.score += 100
			else:
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
		added_item.get_node("ColorRect").color = color_debug[ID+1]
		added_item.item_ID = input_output[ID+1]
		
		
	
