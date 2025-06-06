extends Node2D


'func _ready():

	var joypads = Input.get_connected_joypads()

	for device_id in joypads:
		var axis_value = Input.get_joy_axis(device_id, JOY_AXIS_LEFT_X)
		print("Device", device_id, "Axis:", axis_value)'
		
		

var player1_id = 0
var player2_id = 1

func _process(delta):
	var p1_axis = Input.get_joy_axis(player1_id, JOY_AXIS_LEFT_X)
	var p2_axis = Input.get_joy_axis(player2_id, JOY_AXIS_LEFT_X)

	print("P1:", p1_axis, "P2:", p2_axis)
