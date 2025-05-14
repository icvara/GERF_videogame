extends Control

@export var player: Node2D
var inv_isopen = false
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


	if Input.is_action_just_pressed("inventory"):
		if inv_isopen:
			close_inventory()
		else:
			open_inventory()
			

func close_inventory():
	inv_isopen = false
	hide()
	#get_tree().paused = false
	pass

func open_inventory():
	updateTeam(player)
	inv_isopen = true
	show()
	#get_tree().paused = true
	pass
	



func _on_button_pressed():
	#get_tree().paused = false
	hide()
	
func updateTeam(player):

	for m in player.micromon_inv:
		print(player.micromon_inv[m])
		$Panel/VBoxContainer.get_node(str(m)).get_node("ID").text = m
		$Panel/VBoxContainer.get_node(str(m)).get_node("TextureRect")
		if player.micromon_inv[m] != null:
			$Panel/VBoxContainer.get_node(str(m)).get_node("Label").text = player.micromon_inv[m].micromon_name
		else:
			$Panel/VBoxContainer.get_node(str(m)).get_node("Label").text = "EMPTY"
		if player.micromon_inv[m] != null:
			$Panel/VBoxContainer.get_node(str(m)).get_node("Button"+str(m)).show()
		else:
			$Panel/VBoxContainer.get_node(str(m)).get_node("Button"+str(m)).hide()


func _on_button_1_pressed():
	print(player.micromon_inv)
	player.micromon_inv["1"].Drop("1",player) 
	updateTeam(player)

func _on_button_2_pressed():
	player.micromon_inv["2"].Drop("2",player) 
	updateTeam(player)

func _on_button_3_pressed():
	player.micromon_inv["3"].Drop("3",player) 
	updateTeam(player)


func _on_button_4_pressed():
	player.micromon_inv["4"].Drop("4",player) 
	updateTeam(player)	
	pass # Replace with function body.


func _on_button_5_pressed():
	player.micromon_inv["5"].Drop("5",player) 
	updateTeam(player)

func _on_button_6_pressed():
	player.micromon_inv["6"].Drop("6",player) 
	updateTeam(player)
