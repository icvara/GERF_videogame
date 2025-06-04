extends Node2D

func _ready() -> void:
	$Panel/next1.grab_focus()

func _on_next_1_pressed() -> void:
	$Panel2.show()
	$Panel/next1.hide()
	$Panel2/Button.grab_focus()


func _on_button_pressed() -> void:
	#print("stprxz: " + str(GlobalVariableOverlab.nplayer))
	$Forest.stop()
	get_tree().change_scene_to_file("res://GERF_version/Scenes/level_selector.tscn")
