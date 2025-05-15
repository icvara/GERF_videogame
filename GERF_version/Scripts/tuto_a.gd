extends Control


func _on_button_pressed():
	GlobalVariableOverlab.init_var()
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/overlab/main_overlab.tscn")
