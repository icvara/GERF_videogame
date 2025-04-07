extends CharacterBody2D

var SPEED = 50
var interacting_with
var inventory
@export var playerID = 1

func _physics_process(delta):
	
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
		$AnimatedSprite2D.play("left")
	elif direction.x > 0:
		$AnimatedSprite2D.play("right")
	elif direction.y > 0:
		$AnimatedSprite2D.play("front")
	elif direction.y < 0:
		$AnimatedSprite2D.play("back")
	else:
		$AnimatedSprite2D.stop()
		
	move_and_slide()
	if inventory != null:
		inventory.global_position = global_position
	
	if Input.is_action_just_pressed("space"):
		print(interacting_with)
		print(inventory)
		if interacting_with != null:
			if inventory == null:
				print("emptz")
				interacting_with.PickUP(self)
			else: 
				print("emptz but busy")
				inventory.Drop(self)
				
		elif inventory != null:
			print("non emptz")
			inventory.Drop(self)




func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == "Item":
		interacting_with = body


func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.name == "Item":
		if interacting_with == body:
			interacting_with = null
