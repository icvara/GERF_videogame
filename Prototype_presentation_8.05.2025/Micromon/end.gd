extends Control



func changetext(vartext):
	$ColorRect/Label.text = vartext

func _on_button_pressed() -> void:
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/start_menu.tscn") 
