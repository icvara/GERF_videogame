extends Micromon


func _ready() -> void:
	micromon_name = "cyano."
	$AnimatedSprite2D.play("default")
	
	skills["0"] = "Photosynth."
	skills["1"] = "Toxic"

	
func _on_body_entered(body):
	if body.name == "Player":

		body.interacting_with = self


func _on_body_exited(body):
	if body.name == "Player":
		if body.interacting_with == self:
			body.interacting_with = null


func Doskill(ID,target):
	if ID == 0:
		HP = clamp(HP + 30,0,100)
	elif ID == 1:
		target.HP -= 5
	elif ID == 3:
		pass
