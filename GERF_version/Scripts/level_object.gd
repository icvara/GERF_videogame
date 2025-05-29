extends Node2D

@export var text = "level 1"
@export var level : PackedScene

var player_on_it = []

func _ready() -> void:
	$ColorRect/Label.text = text
	
	
func _on_area_2d_body_entered(body: Node2D) -> void:
	$ColorRect.color = Color(0,0.2,0.2)
	player_on_it.append(body.playerID) #playerID


func _on_area_2d_body_exited(body: Node2D) -> void:
	$ColorRect.color = Color(0.2,0.2,0.2)
	if player_on_it.has(body.playerID):
		player_on_it.erase(body.playerID)


func _process(delta: float) -> void:
	if player_on_it.size()> 0: #NEED TO ADJUST ACCORDING TO WHO IS ON
		if Input.is_action_just_pressed("space"): 
			get_tree().change_scene_to_packed(level)
