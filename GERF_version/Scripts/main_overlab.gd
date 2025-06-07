extends Node2D

var tuto_on = true
var tuto_step = 0
@export var item : PackedScene
@export var player : PackedScene

var init_posvector = [Vector2(0,0), Vector2(1,0),Vector2(0,1),Vector2(1,1)]


func _ready() -> void:	
	GlobalVariableOverlab.tuto_item_player_hand = [0,0,0,0]
	
	if GlobalVariableOverlab.tuto_on == false:
		$CanvasLayer/TimeHUD.get_node("Timer").start(1.0)
		$CanvasLayer/TimeHUD.show()
		$tuto_0.hide()
	else:
		$CanvasLayer/Tuto_control.call_window()


	for i in GlobalVariableOverlab.nplayer:
		var newplay = player.instantiate()
		newplay.playerID = i
		newplay.playerID = GlobalVariableOverlab.player_ID[i]
		print(GlobalVariableOverlab.player_ID)
		newplay.setskin(GlobalVariableOverlab.playerskin[newplay.playerID])
		#newplay.position = 
		$player_startpos.get_node(str(i)).add_child(newplay)
		
func _process(delta: float) -> void:
	#$CanvasLayer/Panel/timelabel.text = "Time Left: " + str(int($GameTimer.time_left)) + "s"
	if GlobalVariableOverlab.time <= 0 :
		$CanvasLayer/TimeHUD.hide()
		$CanvasLayer/End.start()
		
		
		
	if GlobalVariableOverlab.tuto_on:
		if GlobalVariableOverlab.tuto_item_player_hand.has("DNA") and tuto_step==0:
			$tuto_0.hide()
			$tuto_1.show()
			tuto_step = 1
		if GlobalVariableOverlab.tuto_item_player_hand.has("DNAplaced") and tuto_step==1:
			$tuto_1.hide()
			$tuto_2.show()	
			tuto_step = 2
		if GlobalVariableOverlab.tuto_item_player_hand.has("Cell") and tuto_step==2:
			$tuto_2.hide()
			$tuto_3.show()	
			tuto_step = 3
		if GlobalVariableOverlab.tuto_item_player_hand.has("Cellplaced") and tuto_step==3:
			$tuto_3.hide()
			$tuto_4.show()	
			tuto_step = 4
		if GlobalVariableOverlab.tuto_item_player_hand.has("CellReady") and tuto_step==4:
			$tuto_4.hide()
			$tuto_5.show()	
			tuto_step = 5
		if GlobalVariableOverlab.tuto_item_player_hand.has("mCellplaced") and tuto_step==5:
			$tuto_5.hide()
			$tuto_6.show()	
			tuto_step = 6
		if GlobalVariableOverlab.tuto_item_player_hand.has("Bioproduct") and tuto_step==6:
			$tuto_6.hide()
			$tuto_7.show()	
			tuto_step = 7
		if GlobalVariableOverlab.score > 0 and tuto_step==7:
			$tuto_7.hide()
			$tuto_8.show()	
			get_tree().paused = true
			await get_tree().create_timer(0.5).timeout
			$tuto_8/next1.grab_focus()
			tuto_step = 8


func _on_next_1_pressed() -> void:
	$tuto_8.hide()	
	GlobalVariableOverlab.tuto_on = false
	get_tree().paused = false

	get_tree().reload_current_scene()

	'for item in get_tree().get_nodes_in_group("Item"):
		item.queue_free()'
	#$CanvasLayer/TimeHUD.get_node("Timer").start(1.0)
	#$CanvasLayer/TimeHUD.show()
