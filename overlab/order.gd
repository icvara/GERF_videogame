extends Control


func _process(delta: float) -> void:
	$score_value.text = str(GlobalVariableOverlab.score)
