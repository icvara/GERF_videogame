extends Micromon


func _ready() -> void:
	micromon_name = "e.coli"
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
		target.HP -= 10
	elif ID == 1:
		target.HP -= 30
		skills["1"] = null
	elif ID == 3:
		pass
