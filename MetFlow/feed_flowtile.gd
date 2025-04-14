extends FlowTile




func doaction(body):
	if body.get_node("ColorRect").color == Color(0,1,0):
		get_parent().get_parent().get_node("HealthBar").value += 5
		body.get_node("ColorRect").color = Color(0,0,0)
		#print("miam")



func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("food"):
		doaction(body)
	pass
	#doaction(body)


func _on_area_2d_body_exited(body: Node2D) -> void:
	pass
	
