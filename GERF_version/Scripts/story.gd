extends Node2D


func _on_next_1_pressed() -> void:
	$Panel2.show()
	$Panel/next1.hide()


func _on_button_pressed() -> void:
	get_tree().change_scene_to_file("res://GERF_version/Scenes/level_selector.tscn")
