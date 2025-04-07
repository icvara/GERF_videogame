extends Micromon


func _ready() -> void:
	micromon_name = "e.coli"
	$AnimatedSprite2D.play("default")
func _on_body_entered(body):
	if body.name == "Player":

		body.interacting_with = self


func _on_body_exited(body):
	if body.name == "Player":
		if body.interacting_with == self:
			body.interacting_with = null
