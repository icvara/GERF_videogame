extends Control

@export var player: Node2D
@export var enemy: PackedScene


var current_player_ID = 1
var current_micromon_player1 
var current_micromon_player2 


# Called when the node enters the scene tree for the first time.
func _ready():
	
	#hide()
	pass



func Enemy_turn():
	update_hpbar()
	await get_tree().create_timer(.5).timeout
	if $Enemy/ProgressBar.value <= 0.:
		$end.changetext("You Win!")
		$end.show()
		#hide()
		#get_tree().change_scene_to_file("res://Micromon/end.tscn") 
		#$Player/ProgressBar.value = 100
		#$Enemy/ProgressBar.value = 100
	else:
		#$Player/ProgressBar.value -= 20
		current_micromon_player2.Doskill(0,current_micromon_player1)
		update_hpbar()
		await get_tree().create_timer(.5).timeout
		if $Player/ProgressBar.value <= 0.:
			current_player_ID += 1
			update_micromon("Player", str(current_player_ID)) 
	$PanelContainer.show()
	
func Start():
	show()
	var new_en = enemy.instantiate()
	new_en.hide()
	current_micromon_player2 = new_en
	
	
	current_player_ID = 1
	update_micromon("Player", str(current_player_ID))
	get_node("Enemy").get_node("Sprite").play("default")
	
	
	
	
	
func update_micromon(battleID, InvID):
	#get_parent().get_node(battleID).get_node("AnimatedSprite2d")
	if player.micromon_inv[InvID]:
		current_micromon_player1 = player.micromon_inv[InvID]
		get_node(battleID).get_node("Sprite").sprite_frames = player.micromon_inv[InvID].get_node("AnimatedSprite2D").sprite_frames
		get_node(battleID).get_node("Sprite").play("default")
		get_node(battleID).get_node("Label").text = player.micromon_inv[InvID].micromon_name
		update_hpbar()

	else:
		#get_tree().change_scene_to_file("res://Micromon/end.tscn") 
		$end.changetext("You Failed!")
		$end.show()
		#hide()


func update_hpbar():
	$Player/ProgressBar.value = current_micromon_player1.HP
	$Enemy/ProgressBar.value =  current_micromon_player2.HP

func display_attack():
	for i in range(3):
		if current_micromon_player1.skills[str(i)]:
			$PanelAttack.get_node(str(i)).show()
			$PanelAttack.get_node(str(i)).text = current_micromon_player1.skills[str(i)]
		else:
			$PanelAttack.get_node(str(i)).hide()


func _on_button_leave_pressed() -> void:
	hide()


func _on_return_pressed() -> void:
	$PanelAttack.hide() # Replace with function body.
	$PanelContainer.show()


func _on_button_attack_pressed() -> void:
	display_attack()
	$PanelAttack.show()
	$PanelContainer.hide()


func a1_on__pressed() -> void:
	current_micromon_player1.Doskill(0,current_micromon_player2)
	#$Player/ProgressBar.value += 30
	$PanelAttack.hide() 
	Enemy_turn()

func a2_on__pressed() -> void:
	current_micromon_player1.Doskill(1,current_micromon_player2)
	#$Enemy/ProgressBar.value -= 10
	$PanelAttack.hide() 
	Enemy_turn()

func a3_on__pressed() -> void:
	current_micromon_player1.Doskill(2,current_micromon_player2)
	#$Player/ProgressBar.value -= 20
	$PanelAttack.hide() 
	Enemy_turn()
