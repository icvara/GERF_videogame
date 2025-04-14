extends FlowTile


func doaction(body):
	if body.get_node("ColorRect").color == Color(1,0,0):
		body.get_node("ColorRect").color = Color(0,1,0)
		#print("transform")


func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("food"):
		doaction(body)
	pass
	#doaction(body)


func _on_area_2d_body_exited(body: Node2D) -> void:
	pass
