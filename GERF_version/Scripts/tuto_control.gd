extends Control

var tuto_finshed = false

func call_window():
	show()
	get_tree().paused = true
	tuto_finshed = false
	

func _process(delta: float) -> void:
	#if $Panel/ColorRect.finished:
		if tuto_finshed == false:
			$Panel/Button.grab_focus()
			tuto_finshed = true

func _on_button_pressed():
	get_tree().paused = false
	hide()
	
