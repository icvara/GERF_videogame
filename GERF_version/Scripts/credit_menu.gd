extends Control




func _on_1_pressed() -> void:
	get_tree().change_scene_to_file("res://GERF_version/Scenes/starting_menu.tscn") 


func _on_4_pressed() -> void:
	get_tree().quit()


func _on__pressed() -> void:
	pass # Replace with function body.
