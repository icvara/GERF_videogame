extends FlowTile

var state = 0 


func doaction(body):
	if state == 0:
		if body.get_node("ColorRect").color == Color(1,0,0):
			body.get_node("ColorRect").color = Color(0,1,0)
	elif state == 1:
		if body.get_node("ColorRect").color == Color(1,0,0):
			body.get_node("ColorRect").color = Color(0,0,1)
			get_parent().get_parent().get_node("GoalBar").value += 5

			#print("transform")

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("food"):
		doaction(body)
	pass
	#doaction(body)


func _on_area_2d_body_exited(body: Node2D) -> void:
	pass



func do_mouse_action():
	pass
	state += 1
	if state > 1:
		state = 0
	if state == 0:
		$ColorRect.color = Color(1,1,0)
	else:
		$ColorRect.color = Color(1,0,1)
