extends Control

#This script is for the credits of the game

func _ready() -> void:
	$"ColorRect/VBoxContainer/1".grab_focus()



func _on_1_pressed() -> void:
	#when button return is pressed go back to landing page
	get_tree().change_scene_to_file("res://Scenes/starting_menu.tscn") 


func _on_4_pressed() -> void:
	#Quit window/game when quit is pressed
	get_tree().quit()
