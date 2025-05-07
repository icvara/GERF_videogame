extends Control


func _process(delta: float) -> void:
	$Panel/Label.text = "Score: " + str(GlobalVariableOverlab.score)
