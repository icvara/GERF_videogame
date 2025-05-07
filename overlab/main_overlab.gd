extends Node2D


@export var item : PackedScene
@export var player : PackedScene

var init_posvector = [Vector2(0,0), Vector2(1,0),Vector2(0,1),Vector2(1,1)]
func _ready() -> void:
	
	#instance the player
	for i in GlobalVariableOverlab.nplayer:
		var newplay = player.instantiate()
		newplay.setskin(GlobalVariableOverlab.playerskin[i])
		newplay.playerID = i
		newplay.position = Vector2(80,40) + Vector2((320-40)/2,(180-40)/2) * init_posvector[i]
		add_child(newplay)
		
func _process(delta: float) -> void:
	$CanvasLayer/Panel/timelabel.text = "Time Left: " + str(int($GameTimer.time_left)) + "s"





func _on_game_timer_timeout() -> void:
	$CanvasLayer/End.start()
