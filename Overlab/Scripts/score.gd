extends Control

@export var score_for_three = 500

func _process(delta: float) -> void:
	$score_bar/Progress.value = clamp(GlobalVariableOverlab.score *100/score_for_three,0,100)
	$Label.text = "Score: " + str(GlobalVariableOverlab.score)
	update_star()


func update_star():
	if $score_bar/Progress.value >= 20:
		$score_bar/FullStar.show()
		
		if $score_bar/Progress.value>= 50:
			$score_bar/FullStar2.show()
			
			if $score_bar/Progress.value >= 90:
				$score_bar/FullStar3.show()
