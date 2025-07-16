extends Control

@export var time_total = 80.0

var changemusic = false

func _ready() -> void:
	GlobalVariableOverlab.time = time_total
	



func _process(delta: float) -> void:
	$ProgressBar.value = GlobalVariableOverlab.time
	$timevalue.text = str(GlobalVariableOverlab.time) +"s"
	'if GlobalVariableOverlab.time < 10 :
		if changemusic == true:
				$CaveTheme.pitch_scale = 1.4
				changemusic = false'
	if GlobalVariableOverlab.time < 25 :
		$ProgressBar.modulate = Color(1,0,0)
		if changemusic == false:
			$CaveTheme.stop()
			#$CaveTheme.pitch_scale = 1.
			$Dark_soundwave.play()
			changemusic = true

	else: 
		$ProgressBar.modulate = Color(0,1,0)
	
	



func _on_timer_timeout() -> void:
	GlobalVariableOverlab.time -= 1
	GlobalVariableOverlab.time = clamp(GlobalVariableOverlab.time,0,time_total)
