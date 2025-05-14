extends Control


func start():
	show()
	$Label2.text = "Score: " + str(GlobalVariableOverlab.score)
	
	if GlobalVariableOverlab.score < 300:
		$Label3.text = "Not Impressive"
	elif GlobalVariableOverlab.score > 900:
		$Label3.text = "Awesome TeamWork"
	else:
		$Label3.text = "Good Job!"	


func _on_button_pressed() -> void:
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/start_menu.tscn") 
