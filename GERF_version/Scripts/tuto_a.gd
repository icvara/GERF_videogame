extends Control


func _on_button_pressed():
	GlobalVariableOverlab.init_var()
	get_tree().change_scene_to_file("res://GERF_version/Scenes/main_overlab.tscn")
