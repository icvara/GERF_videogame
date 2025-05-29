extends Control

@export var player : PackedScene

func _ready() -> void:
	$Tuto_control.call_window()
	init_player()

func init_player():
	for i in GlobalVariableOverlab.nplayer:
		var newplay = player.instantiate()
		newplay.setskin(GlobalVariableOverlab.playerskin[i])
		newplay.playerID = i
		#newplay.position = Vector2(260,50) + Vector2(-(320-40)/2,(180-40)/2) * init_posvector[i]
		$startposplayer.add_child(newplay)
		newplay.position =  Vector2(32,0) * i
