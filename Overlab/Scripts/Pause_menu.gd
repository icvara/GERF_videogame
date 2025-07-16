extends Control


var paused = false


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("pause"):
		print("here")

		if paused == false:
			print("here2")
			show()

			$Panel/VBoxContainer/Button.grab_focus()
			paused = true
			get_tree().paused = true


func _on_button_pressed():
	pass # Replace with function body.
	paused = false
	hide()
	get_tree().paused = false


func _on_button_2_pressed():
	pass # Replace with function body.
	#get_tree().change_scene_to_file("res://start_menu.tscn") 
	get_tree().paused = false
	paused = false

	GlobalVariableOverlab.score = 0
	get_tree().reload_current_scene()
	

func _on_button_4_pressed():
	get_tree().paused = false
	paused = false

	get_tree().change_scene_to_file("res://Scenes/starting_menu.tscn") 

	#get_tree().quit()
	

	


func _on_button_3_pressed() -> void:
	paused = false

	$Panel.hide()
	
	$Control.show()
	$Control/Button_crtl.grab_focus()


func _on_button_crtl_pressed() -> void:
	$Control.hide()
	hide()

	get_tree().paused = false
