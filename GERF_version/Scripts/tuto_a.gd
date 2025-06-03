extends Control

func _ready() -> void:
	$ColorRect/Button.grab_focus()


func _on_button_pressed():
	get_tree().change_scene_to_file("res://GERF_version/Scenes/level_1.tscn")
