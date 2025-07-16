extends Node2D

@export var player : PackedScene


func _ready() -> void:
	#$Tuto_control.call_window()
	for i in GlobalVariableOverlab.nplayer:
		var newplay = player.instantiate()
		newplay.playerID = i
		newplay.playerID = GlobalVariableOverlab.player_ID[i]
		newplay.setskin(GlobalVariableOverlab.playerskin[newplay.playerID])
		#newplay.position = 
		$player_startpos.get_node(str(i)).add_child(newplay)
