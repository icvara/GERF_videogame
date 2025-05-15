extends CharacterBody2D

var player_holding

var item_ID = "DNA"

func PickUP(player):
	#player.add_child(self)
	if player.inventory == null:
		player.inventory = self
		player_holding = player
		#linear_damp = 0
		set_collision_layer_value(1,false)

		#set_physics_process(false)


func Drop(player):
	if player.inventory != null:
		player.inventory = null
		player_holding = null
	
		#linear_damp = 10
		set_collision_layer_value(1,true)
		#set_physics_process(true)
	#get_parent().get_parent().add_child(self)


func _physics_process(delta: float) -> void:
	if player_holding:
		pass#apply_central_impulse(player_holding.velocity)

'func _process(delta: float) -> void:
	if player_holding:
		position = player_holding.position'
