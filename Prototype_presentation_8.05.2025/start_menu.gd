extends Control


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_button_pressed():
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/MetFlow/main_metflow.tscn")


func _on_button_2_pressed():
	#get_tree().change_scene_to_file("res://Micromon/main_micromon.tscn")
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/Micromon/micromon_start.tscn")


func _on_button_3_pressed() -> void:
	#get_tree().change_scene_to_file("res://overlab/main_overlab.tscn")
	GlobalVariableOverlab.init_var()
	get_tree().change_scene_to_file("res://Prototype_presentation_8.05.2025/overlab/player_select.tscn")


func _on_button_4_pressed() -> void:
	get_tree().quit()
