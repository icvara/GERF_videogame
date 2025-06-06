extends ColorRect

var joy_button_pressed = false
var step = 1
var finished = false

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
			if !joy_button_pressed:
				joy_button_pressed = true 
				
				if step <5:
					$Label.hide()
					get_node(str(step)).show()
					step+= 1
				if step == 5:
					finished = true
				
	else:
				joy_button_pressed = false
