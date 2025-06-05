extends CharacterBody2D

var SPEED = 500
var last_dir = Vector2(0,0)
var interacting_with
var interacting_with_workstation
var interacting_array = []
var inventory
var push_force =  500
var push_velocity = Vector2(0,0)
@export var playerID = 1

var animatedstuff

func setskin(skinid):
	animatedstuff = get_node("AnimatedSprite2D_"+str(skinid))
	animatedstuff.show()
	get_node("Circle"+ str(playerID+1)).show()

func get_closest_element(list: Array, target: Vector2) :

	var closest = list[0]
	var centre_pos =  closest.global_position + Vector2(16,16)
	var min_diff = centre_pos.distance_to(target)
	for element in list:
		centre_pos =  element.global_position + Vector2(16,16)
		var diff = centre_pos.distance_to(target)
		if diff < min_diff:
			min_diff = diff
			closest = element
	return closest



func _physics_process(delta):
	

	
	#if GlobalVariableOverlab.nplayer >= 1:
	if Input.is_action_just_pressed("change_player"):
			if playerID == 1:
				playerID = 0
			else:
				playerID = 1
		
	if 	animatedstuff.is_visible() == false:
		animatedstuff.show()

	var direction = null
	if GlobalVariableOverlab.nplayer >= 2:
		if playerID == 0:
			direction = Vector2(Input.get_axis("left", "right"),Input.get_axis("up", "down"))
		elif playerID == 1: 
			direction = Vector2(Input.get_axis("left2", "right2"),Input.get_axis("up2", "down2"))
		else: 
			direction = Vector2(Input.get_axis("left3", "right3"),Input.get_axis("up3", "down3"))
	else:
		direction = Vector2()
		direction += Vector2(Input.get_axis("left", "right"),Input.get_axis("up", "down"))
		direction += Vector2(Input.get_axis("left2", "right2"),Input.get_axis("up2", "down2"))
		direction += Vector2(Input.get_axis("left3", "right3"),Input.get_axis("up3", "down3"))
		direction = direction.normalized()
		
	if direction:
		velocity = direction * SPEED 
	else:
		velocity = Vector2(0,0) 
	
	if direction.x < 0:		
		animatedstuff.play("left")
		last_dir = direction
	elif direction.x > 0:
		animatedstuff.play("right")
		last_dir = direction
	elif direction.y > 0:
		animatedstuff.play("front")
		last_dir = direction
	elif direction.y < 0:
		animatedstuff.play("back")
		last_dir = direction
	else:
		animatedstuff.stop()
	
	
	
	
	for i in get_slide_collision_count():
		var c = get_slide_collision(i)
		if c.get_collider() is CharacterBody2D:
			var push_direction = velocity.normalized()
			velocity += c.get_collider().velocity.normalized() * push_force
			c.get_collider().velocity += push_direction * push_force
	
	move_and_slide()

	
	if inventory != null:
		#inventory.apply_central_force(velocity)
		#inventory.global_position = global_position
		inventory.position = global_position + Vector2(-8,0)

	if interacting_array.size() > 0:
		var closest_station = get_closest_element(interacting_array,global_position + last_dir*32)
		if interacting_with_workstation:
			if interacting_with_workstation != closest_station:
				if interacting_with_workstation.get_node("ColorRect"):
					interacting_with_workstation.get_node("ColorRect").hide()
				interacting_with_workstation = closest_station
				if closest_station.get_node("ColorRect"):
					closest_station.get_node("ColorRect").show()
		else:
			interacting_with_workstation = closest_station
			if closest_station.get_node("ColorRect"):
					closest_station.get_node("ColorRect").show()



	if GlobalVariableOverlab.nplayer >= 2:
		if playerID == 0:
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
		elif playerID == 1:	
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

		elif playerID == 2:	
			if Input.is_action_just_pressed("space3"):
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
		if Input.is_action_just_pressed("space") or Input.is_action_just_pressed("space2") or Input.is_action_just_pressed("space3") :
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
		interacting_array.append(body)
		'if interacting_with_workstation:
			if interacting_with_workstation.get_node("ColorRect"):
				interacting_with_workstation.get_node("ColorRect").hide()
		interacting_with_workstation = body 
		if body.get_node("ColorRect"):
			body.get_node("ColorRect").show()'
	

func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.is_in_group("Item"):
		if interacting_with == body:
			interacting_with = null
	if body.is_in_group("workstation"):
		if 	interacting_array.has(body):
				interacting_array.erase(body)


		if interacting_with_workstation == body:
			interacting_with_workstation = null 
			if body.get_node("ColorRect"):
				body.get_node("ColorRect").hide()
			
func displaymsg(textstr):
	$Label.text = textstr
	$Label.show()
	await get_tree().create_timer(.5).timeout
	$Label.hide()
