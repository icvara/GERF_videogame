extends CharacterBody2D

var SPEED = 50
var interacting_with
var interacting_with_workstation
var inventory
var push_force =  80
@export var playerID = 1



func _physics_process(delta):
	if 	get_node("AnimatedSprite2D_"+str(playerID)).is_visible() == false:
		get_node("AnimatedSprite2D_"+str(playerID)).show()

	var direction = null
	if playerID == 1:
		direction = Vector2(Input.get_axis("left", "right"),Input.get_axis("up", "down"))
	else: 
		direction = Vector2(Input.get_axis("left2", "right2"),Input.get_axis("up2", "down2"))

	if direction:
		velocity = direction * SPEED
	else:
		velocity = Vector2(0,0)
	
	if direction.x < 0:		
		get_node("AnimatedSprite2D_"+str(playerID)).play("left")
	elif direction.x > 0:
		get_node("AnimatedSprite2D_"+str(playerID)).play("right")
	elif direction.y > 0:
		get_node("AnimatedSprite2D_"+str(playerID)).play("front")
	elif direction.y < 0:
		get_node("AnimatedSprite2D_"+str(playerID)).play("back")
	else:
		get_node("AnimatedSprite2D_"+str(playerID)).stop()
		
	move_and_slide()
	
	for i in get_slide_collision_count():
		var c = get_slide_collision(i)
		if c.get_collider() is RigidBody2D:
			c.get_collider().apply_central_impulse(-c.get_normal()*push_force)
	
	if inventory != null:
		#inventory.apply_central_force(velocity)
		inventory.global_position = global_position
	
	if playerID == 1:
		if Input.is_action_just_pressed("space"):
			if interacting_with_workstation:
				interacting_with_workstation.Use(self)
			else:
				if interacting_with != null:
					if inventory == null:
						interacting_with.PickUP(self)
					else: 
						inventory.Drop(self)
				elif inventory != null:
					inventory.Drop(self)
			
			
	else:
		if Input.is_action_just_pressed("space2"):
			if interacting_with_workstation:
				interacting_with_workstation.Use(self)
			else:
				if interacting_with != null:
					if inventory == null:
						interacting_with.PickUP(self)
					else: 
						inventory.Drop(self)
				elif inventory != null:
					inventory.Drop(self)




func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("Item"):
		interacting_with = body
	if body.is_in_group("workstation"):
		interacting_with_workstation = body 


func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.is_in_group("Item"):
		if interacting_with == body:
			interacting_with = null
	if body.is_in_group("workstation"):
		if interacting_with_workstation == body:
			interacting_with_workstation = null 
