extends Control

@export var player: Node2D

# Called when the node enters the scene tree for the first time.
func _ready():
	#hide()
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass



func Start():
	show()
	update_micromon("Player", "1")
	get_node("Enemy").get_node("Sprite").play("default")

	
	
	
func update_micromon(battleID, InvID):
	#get_parent().get_node(battleID).get_node("AnimatedSprite2d")
	if player.micromon_inv[InvID]:
		get_node(battleID).get_node("Sprite").sprite_frames = player.micromon_inv[InvID].get_node("AnimatedSprite2D").sprite_frames
		get_node(battleID).get_node("Sprite").play("default")
		get_node(battleID).get_node("Label").text = player.micromon_inv[InvID].micromon_name
	


func _on_button_leave_pressed() -> void:
	hide()


func _on_return_pressed() -> void:
	$PanelAttack.hide() # Replace with function body.


func _on_button_attack_pressed() -> void:
	$PanelAttack.show()


func a1_on__pressed() -> void:
	$Player/ProgressBar.value += 20


func a2_on__pressed() -> void:
	$Enemy/ProgressBar.value -= 40


func a3_on__pressed() -> void:
	$Player/ProgressBar.value -= 20
