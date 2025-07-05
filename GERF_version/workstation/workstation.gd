extends StaticBody2D
class_name Workstation

@export var item: PackedScene

var added_item
var task_finshed = false
var size = Vector2(1,1)


func Use(player):
	pass
	
func _on_timer_timeout() -> void:
	pass
		
		
	
func displaytext(msg):
	$Label.text = msg
	$Label.show()
	await get_tree().create_timer(.5).timeout
	$Label.hide()
