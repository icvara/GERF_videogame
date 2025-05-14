extends Control


func _on_button_pressed() -> void:
	if $Label.is_visible() :
		$Label.hide() 

	else:
		$Label.show()
		
