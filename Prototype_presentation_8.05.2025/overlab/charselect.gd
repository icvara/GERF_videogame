extends Control

var player_skinid = 0
var skin_number = 2 
@export var player_number = 1
var char_added = false
var joy_button_pressed = false

func _ready() -> void:
	$AnimatedSprite2D.play(str(0))
	$Label.text = "Player " + str(player_number)
	'if player_number == 1:
		$Label2.text = "Press (A) to join"
	if player_number == 2:
		$Label2.text = "Press SPACE to join"

	if player_number == 3:
		$Label2.text = "Press SHIFT to join"'



func add_player_choice():
	if !char_added:
		char_added = true
		$Label2.hide()	
		$Label3.show()
		$AnimatedSprite2D.show()
		get_node("Circle"+ str(player_number)).show()
		$Label.show()
		GlobalVariableOverlab.nplayer = clamp(GlobalVariableOverlab.nplayer+1,0,4)	
		GlobalVariableOverlab.player_ID.append(player_number-1)


func remove_player_choice():
	if char_added:
		char_added = false
		$Label2.show()	
		$Label3.hide()
		$AnimatedSprite2D.hide()
		get_node("Circle"+ str(player_number)).hide()
		$Label.hide()
		GlobalVariableOverlab.nplayer = clamp(GlobalVariableOverlab.nplayer-1,0,4)	
		GlobalVariableOverlab.player_ID.erase(player_number-1)

		
func _process(delta: float) -> void:
	if player_number == 1:
		if Input.is_action_just_pressed("space"):
			add_player_choice()
		#if Input.is_action_just_pressed("up") or Input.is_action_just_pressed("down") or Input.is_action_just_pressed("right") or Input.is_action_just_pressed("left"):
			
	elif player_number == 2:
		if Input.is_action_just_pressed("space2"):
			add_player_choice()
		'if Input.is_action_just_pressed("up2") or Input.is_action_just_pressed("down2"):
			$L.grab_focus()'
	elif player_number == 3:
		if Input.is_action_just_pressed("space3"):
			add_player_choice()
		'if Input.is_action_just_pressed("up3") or Input.is_action_just_pressed("down3"):
			$L.grab_focus()'

	if Input.is_joy_button_pressed(player_number-1, 1):
		remove_player_choice()		
	
	if Input.is_joy_button_pressed(player_number-1, 0):
		add_player_choice()	
	
	if Input.is_joy_button_pressed(player_number-1, 3):
		if !joy_button_pressed:
			joy_button_pressed = true 
			player_skinid += 1
			if player_skinid > skin_number:
				player_skinid = 0
			$AnimatedSprite2D.play(str(player_skinid))
			GlobalVariableOverlab.playerskin[player_number-1]=player_skinid

	else:
			joy_button_pressed = false


func _on_r_pressed() -> void:
	#player_skinid = clamp (player_skinid+1,0,1)
	player_skinid += 1
	if player_skinid > skin_number:
		player_skinid = 0
	$AnimatedSprite2D.play(str(player_skinid))
	GlobalVariableOverlab.playerskin[player_number-1]=player_skinid

func _on_l_pressed() -> void:
	#player_id = clamp (player_skinid-1,0,1)
	player_skinid -= 1
	if player_skinid < 0:
		player_skinid = skin_number
	$AnimatedSprite2D.play(str(player_skinid))
	GlobalVariableOverlab.playerskin[player_number-1]=player_skinid
