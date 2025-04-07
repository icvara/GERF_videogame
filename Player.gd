extends CharacterBody2D


const SPEED = 50.0

var inv_isopen = false
var micromon_inv = { "1": null,
					"2": null,
					"3":null,
					"4":null,
					"5":null,
					"6":null
						}

var is_inFight = false
var interacting_with: Micromon


func _physics_process(delta):

	if Input.is_action_just_pressed("up"):
		velocity.y = SPEED

	
	var direction = Vector2(Input.get_axis("left", "right"),Input.get_axis("up", "down"))
	if direction:
		velocity = direction * SPEED
	else:
		velocity = Vector2(0,0)
	
	if direction.x < 0:
		$AnimatedSprite2D.play("left")
	elif direction.x > 0:
		$AnimatedSprite2D.play("right")
	else:
		$AnimatedSprite2D.stop()


	move_and_slide()
	
	if Input.is_action_just_pressed("space"):
		if interacting_with != null:
			interacting_with.PickUp(self)
	
	
	if Input.is_action_just_pressed("fight"):
		is_inFight = true
		get_parent().get_node("CanvasLayer").get_node("Fight_scene").Start()
