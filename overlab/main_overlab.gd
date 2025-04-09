extends Node2D


@export var item : PackedScene




func _on_timer_timeout() -> void:
	var new_item = item.instantiate()
	add_child(new_item)
	new_item.position = Vector2(randi_range(280,300),randi_range(50,80))
