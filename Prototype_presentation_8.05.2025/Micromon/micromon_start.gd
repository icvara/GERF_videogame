extends Control

var numberplayer = 1

func _on_button_pressed() -> void:
	$SpriteSelect2.hide()
	numberplayer = 1

func _on_button_2_pressed() -> void:
	$SpriteSelect2.show()
	numberplayer = 2


func _on_buttonstart_pressed() -> void:
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/Micromon/main_micromon.tscn")
