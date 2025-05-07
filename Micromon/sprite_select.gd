extends Control

var player_skinid = 0
var skin_number = 2 
@export var player_number = 1


func _ready() -> void:
	$AnimatedSprite2D.play(str(player_number-1))
	$Label.text = "Player " + str(player_number)
	

func _on_r_pressed() -> void:
	#player_skinid = clamp (player_skinid+1,0,1)
	player_skinid += 1
	if player_skinid > skin_number:
		player_skinid = 0
	$AnimatedSprite2D.play(str(player_skinid))

func _on_l_pressed() -> void:
	#player_id = clamp (player_skinid-1,0,1)
	player_skinid -= 1
	if player_skinid < 0:
		player_skinid = skin_number
	$AnimatedSprite2D.play(str(player_skinid))
