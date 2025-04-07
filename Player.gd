extends CharacterBody2D


const SPEED = 300.0

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


	move_and_slide()
	
	if Input.is_action_just_pressed("space"):
		if interacting_with != null:
			interacting_with.PickUp(self)
	
	
	if Input.is_action_just_pressed("fight"):
		is_inFight = true
		get_parent().get_node("Fight_scene").Start()

