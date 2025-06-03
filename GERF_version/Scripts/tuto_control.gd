extends Control

func call_window():
	show()
	get_tree().paused = true

func _ready() -> void:
	$Panel/Button.grab_focus()

func _on_button_pressed():
	get_tree().paused = false
	hide()
	
