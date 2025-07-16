extends Node2D

var state = 0
var previous_score = 0

func _process(delta: float) -> void:
	'if Input.is_action_just_pressed("space"):
		GlobalVariableOverlab.score += 100'
	if GlobalVariableOverlab.score != previous_score:
		previous_score = GlobalVariableOverlab.score
		if $floor.get_node(str(state)):
			$floor.get_node(str(state)).show()
		if $wall.get_node(str(state)):
			$wall.get_node(str(state)).show()
		if $Decor.get_node(str(state)):
			$Decor.get_node(str(state)).show()
		if $Life.get_node(str(state)):
			$Life.get_node(str(state)).show()
		state += 1
			
