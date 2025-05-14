extends Micromon


func _ready() -> void:
	micromon_name = "BOSS"
	$AnimatedSprite2D.play("default")
	
	skills["0"] = "Oxydation"
	skills["1"] = "Glycolysis"
	
func _on_body_entered(body):
	if body.name == "Player":

		body.interacting_with = self


func _on_body_exited(body):
	if body.name == "Player":
		if body.interacting_with == self:
			body.interacting_with = null


func Doskill(ID,target):
	if ID == 0:
		target.HP -= 20
	elif ID == 1:
		pass
	elif ID == 3:
		pass
