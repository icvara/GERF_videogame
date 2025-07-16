extends ColorRect

var joy_button_pressed = false
var step = 0
var finished = false

func _process(delta: float) -> void:
	
	
	'if GlobalVariableOverlab.tuto_item_player_hand.has("DNA"):
		print(step)
		$test.show()
		#get_node("0").show()
		step= 1'
	
	'if step == 1:
		if GlobalVariableOverlab.tuto_item_player_hand.has("DNA"):
			get_node(str(step)).show()
			step= 2
	if step == 2:
		if GlobalVariableOverlab.tuto_item_player_hand.has("Cell"):
			get_node(str(step)).show()
			step= 3'
		
	
	if Input.is_action_just_pressed("ui_accept"):
			if !joy_button_pressed:
				joy_button_pressed = true 
				
				if step <2:
					$Label.hide()
					#get_node(str(step)).show()
					#step+= 1
				'if step == 5:
					finished = true'
				
	else:
				joy_button_pressed = false
