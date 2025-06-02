extends Control

@export var time_total = 80.0

func _ready() -> void:
	GlobalVariableOverlab.time = time_total
	$Timer.start(1.0)

func _process(delta: float) -> void:
	$ProgressBar.value = GlobalVariableOverlab.time
	$timevalue.text = str(GlobalVariableOverlab.time) +"s"
	if GlobalVariableOverlab.time < 25 :
		$ProgressBar.modulate = Color(1,0,0)
	else: 
		$ProgressBar.modulate = Color(0,1,0)
	
	



func _on_timer_timeout() -> void:
	GlobalVariableOverlab.time -= 1
	GlobalVariableOverlab.time = clamp(GlobalVariableOverlab.time,0,time_total)
