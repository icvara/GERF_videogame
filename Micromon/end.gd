extends Control



func changetext(vartext):
	$ColorRect/Label.text = vartext

func _on_button_pressed() -> void:
	get_tree().change_scene_to_file("res://start_menu.tscn") 
