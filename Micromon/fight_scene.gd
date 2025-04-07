extends Control

@export var player: Node2D

var current_player_ID = 1

# Called when the node enters the scene tree for the first time.
func _ready():
	#hide()
	pass



func Enemy_turn():
	await get_tree().create_timer(.5).timeout
	if $Enemy/ProgressBar.value <= 0.:
		hide()
		$Player/ProgressBar.value = 100
		$Enemy/ProgressBar.value = 100
	else:
		$Player/ProgressBar.value -= 20
		await get_tree().create_timer(.5).timeout
		if $Player/ProgressBar.value <= 0.:
			current_player_ID += 1
			update_micromon("Player", str(current_player_ID)) 
			$Player/ProgressBar.value = 100

func Start():
	show()
	current_player_ID = 1
	update_micromon("Player", str(current_player_ID))
	get_node("Enemy").get_node("Sprite").play("default")

	
	
	
func update_micromon(battleID, InvID):
	#get_parent().get_node(battleID).get_node("AnimatedSprite2d")
	if player.micromon_inv[InvID]:
		get_node(battleID).get_node("Sprite").sprite_frames = player.micromon_inv[InvID].get_node("AnimatedSprite2D").sprite_frames
		get_node(battleID).get_node("Sprite").play("default")
		get_node(battleID).get_node("Label").text = player.micromon_inv[InvID].micromon_name
	else:
		hide()



func _on_button_leave_pressed() -> void:
	hide()


func _on_return_pressed() -> void:
	$PanelAttack.hide() # Replace with function body.
	$PanelContainer.show()


func _on_button_attack_pressed() -> void:
	$PanelAttack.show()
	$PanelContainer.hide()


func a1_on__pressed() -> void:
	$Player/ProgressBar.value += 20
	Enemy_turn()

func a2_on__pressed() -> void:
	$Enemy/ProgressBar.value -= 40
	Enemy_turn()

func a3_on__pressed() -> void:
	$Player/ProgressBar.value -= 20
	Enemy_turn()
