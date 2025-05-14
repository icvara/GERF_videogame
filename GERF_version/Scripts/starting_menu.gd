extends Control




func _on_1_pressed() -> void:
	pass # Replace with function body.
	GlobalVariableOverlab.init_var()
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/overlab/player_select.tscn")

func _on_2_pressed() -> void:
	pass # Replace with function body.


func _on_3_pressed() -> void:
		get_tree().change_scene_to_file("res://GERF_version/Scenes/credit_menu.tscn")



func _on_4_pressed() -> void:
	get_tree().quit()
