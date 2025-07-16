extends Control

var maxplayer = 4

func _ready():
	GlobalVariableOverlab.player_ID = []

func _process(delta: float) -> void:
	if GlobalVariableOverlab.nplayer > 0 :
		$ProgressBar.show()
		$Label3.show()
		$Buttonstart.show()
	else:
		$ProgressBar.hide()
		$Label3.hide()
		$Buttonstart.hide()
	
	if Input.is_action_pressed("start_game"):
		$ProgressBar.value += 1
	else:
		$ProgressBar.value = 0
	
	if $ProgressBar.value == $ProgressBar.max_value:
		get_tree().change_scene_to_file("res://Scenes/level_1.tscn")

func _on_buttonstart_pressed() -> void:
	GlobalVariableOverlab.tuto_on = true
	get_tree().change_scene_to_file("res://Scenes/level_1.tscn")
