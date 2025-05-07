extends StaticBody2D
class_name Workstation

var added_item
var task_finshed = false



func Use(player):
	pass
	
func _on_timer_timeout() -> void:
	pass
		
		
	
func displaytext(msg):
	$Label.text = msg
	$Label.show()
	await get_tree().create_timer(.5).timeout
	$Label.hide()
