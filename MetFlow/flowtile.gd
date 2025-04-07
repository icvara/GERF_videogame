extends Node2D
class_name FlowTile

var col = Color(1,0,0)

enum ShapeType {Line, T, Split}
var number_of_shape = 3
var ismoving = false
var clicked = false
var current_shape = ShapeType.Line

# Called when the node enters the scene tree for the first time.
func _ready():
	shape_activation(true)



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if ismoving:
		position =  get_global_mouse_position() # - get_parent().get_parent().position
	
	






func get_current_shape():
	var shape = $Shape.get_node(str(current_shape))
	return shape

func switch_shape():
	shape_activation(false)
	var new
	if current_shape + 1 < number_of_shape:
		new = current_shape+1
	else:
		new = 0		
	current_shape = new
	shape_activation(true)
	
func shape_activation(truefalse):
	get_current_shape().set_collision_layer_value(1,truefalse)
	get_current_shape().set_collision_mask_value(1,truefalse)
	get_current_shape().visible = truefalse


func _on_button_gui_input(event):

		if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
			if event.pressed:
				switch_shape()				


		if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_RIGHT:
			if event.pressed:
				get_current_shape().rotation += deg_to_rad(90)


	
