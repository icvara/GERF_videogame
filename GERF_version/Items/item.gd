extends RigidBody2D
class_name Item

var player_holding

@export var item_ID = "DNA"
var test

func PickUP(player):
	#player.add_child(self)
	if player.inventory == null:
		freeze_mode = 0
		linear_velocity = Vector2(0,0)

		player.inventory = self
		player_holding = player
		#linear_damp = 0
		set_collision_layer_value(1,false)
		print("pick up")
		z_index = 1

		#set_physics_process(false)


func Drop(player):
	if player.inventory != null:
		freeze_mode = 1
		linear_velocity = Vector2(0,0)

		player.inventory = null
		player_holding = null
	
		#linear_damp = 10
		set_collision_layer_value(1,true)
		z_index = 0
		#set_physics_process(true)
	#get_parent().get_parent().add_child(self)


func Transfer(player):
	if player.inventory != null:
		queue_free()
	'	freeze_mode = 0
		linear_velocity = Vector2(0,0)
		player.inventory = null
		player_holding = null
	
		#linear_damp = 10
		set_collision_layer_value(1,false)
		set_collision_mask_value(1,false)

		z_index = 1'
		#set_physics_process(true)
	#get_parent().get_parent().add_child(self)


func _process(delta: float) -> void:
	pass
	#print(global_position)
	test = global_position
	if player_holding:
		pass#apply_central_impulse(player_holding.velocity)
	
func _physics_process(delta: float) -> void:
	
	if player_holding:
		pass#apply_central_impulse(player_holding.velocity)

'func _process(delta: float) -> void:
	if player_holding:
		position = player_holding.position'
