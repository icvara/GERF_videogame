extends Node2D

@export var item : PackedScene
@export var player : PackedScene

var init_posvector = [Vector2(0,0), Vector2(1,0),Vector2(0,1),Vector2(1,1)]


func _ready() -> void:	
	#instance the player
	#GlobalVariableOverlab.nplayer = 3
	print("ss")
	print(GlobalVariableOverlab.nplayer)
	for i in GlobalVariableOverlab.nplayer:
		var newplay = player.instantiate()
		newplay.setskin(GlobalVariableOverlab.playerskin[i])
		newplay.playerID = i
		#newplay.position = 
		$player_startpos.get_node(str(i)).add_child(newplay)
		
func _process(delta: float) -> void:
	#$CanvasLayer/Panel/timelabel.text = "Time Left: " + str(int($GameTimer.time_left)) + "s"
	if GlobalVariableOverlab.time <= 0 :
		$CanvasLayer/TimeHUD.hide()
		$CanvasLayer/End.start()




	
