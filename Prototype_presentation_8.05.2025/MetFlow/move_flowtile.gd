extends FlowTile


var direction = Vector2(1,0)
var dir_array = [Vector2(1,0),Vector2(0,1),Vector2(-1,0),Vector2(0,-1)]
var arrow_array = [">","|","<","^"]
@export var dir_index = 0

var force = 10

func doaction(body):
	body.apply_impulse(force*direction)

func _ready():
	pass
	#$ColorRect.color = Color(randf_range(0,1),0,0)
	grid_snatch()
	direction = dir_array[dir_index]
	$Label.text = arrow_array[dir_index]

func do_mouse_action():
	dir_index += 1
	if dir_index > 3:
		dir_index = 0
	direction = dir_array[dir_index]
	$Label.text = arrow_array[dir_index]


func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("food"):
		doaction(body)
	pass
	#doaction(body)


func _on_area_2d_body_exited(body: Node2D) -> void:
	pass
