extends Node2D

func _ready() -> void:
	pass

func _process(delta: float) -> void:
	$CanvasLayer/annoncement.text = "Fight Start in " + str(int($Timer.time_left)) + "s - Press F to start Fight"
	if Input.is_action_just_pressed("fight"):
		#is_inFight = true
		$Timer.stop()
		get_node("CanvasLayer").get_node("Fight_scene").Start()

func _on_timer_timeout() -> void:
	#is_inFight = true
	get_node("CanvasLayer").get_node("Fight_scene").Start()
