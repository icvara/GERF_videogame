extends Control

var maxplayer = 2

func _on_r_pressed() -> void:
	GlobalVariableOverlab.nplayer = clamp (GlobalVariableOverlab.nplayer+1,1,maxplayer)
	$HBoxContainer/Label.text = str(GlobalVariableOverlab.nplayer)
	$HBoxContainer2.get_node("charselect"+str(GlobalVariableOverlab.nplayer)).show()


func _on_l_pressed() -> void:
	if GlobalVariableOverlab.nplayer != 1:
		$HBoxContainer2.get_node("charselect"+str(GlobalVariableOverlab.nplayer)).hide()
	GlobalVariableOverlab.nplayer = clamp (GlobalVariableOverlab.nplayer-1,1,maxplayer)
	$HBoxContainer/Label.text = str(GlobalVariableOverlab.nplayer)


func _on_buttonstart_pressed() -> void:
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/overlab/main_overlab.tscn")
