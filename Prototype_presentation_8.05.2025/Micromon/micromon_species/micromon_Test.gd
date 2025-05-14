extends Micromon



func _on_body_entered(body):
	if body.name == "Player":

		body.interacting_with = self


func _on_body_exited(body):
	if body.name == "Player":
		if body.interacting_with == self:
			body.interacting_with = null
