extends Control

#This script is for the landing menu of the game






func _ready() -> void:
	$"ColorRect/VBoxContainer/1".grab_focus()
	
func _on_1_pressed() -> void:
	GlobalVariableOverlab.init_var()

	#when start is pressed launch the game
	#Currently still calling the old version used for the last presentation. it will be change soon.
	get_tree().change_scene_to_file("res://GERF_version/Scenes/player_select.tscn")


	#get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/overlab/player_select.tscn")

func _on_2_pressed() -> void:
	#extra button if needed. no function yet
	pass


func _on_3_pressed() -> void:
	#when credits is pressed, display the credit
	#could also be possible to have them present in the landing page , without having to press a button.
	get_tree().change_scene_to_file("res://GERF_version/Scenes/credit_menu.tscn")



func _on_4_pressed() -> void:
	#Quit window/game when quit is pressed
	get_tree().quit()
