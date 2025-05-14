extends Micromon


func _ready() -> void:
	micromon_name = "Yarrowia"
	$AnimatedSprite2D.play("default")
	
	skills["0"] = "Fatty Acid"
	skills["1"] = "Oxydation"
	skills["2"] = "Biofilm"


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
		HP -= 5
		#skills["1"] = null
	elif ID == 2:
		HP += 18
