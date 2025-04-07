extends Node2D

@export var newtile: PackedScene
@export var newfluid: PackedScene

var cell_flow_size = Vector2(240,124)#$Yeast/flowarea.

# Called when the node enters the scene tree for the first time.
func _ready():
	fill_the_cell()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass





func fill_the_cell():
	var n_tile = cell_flow_size/8/2
	for i in n_tile.x:
		for j in n_tile.y:
			var nt = newtile.instantiate()
			nt.position = Vector2(i*8*2,j*8*2) 
			#if randi_range(0, 1) == 1:		
				#nt.get_node("StaticBody2D").rotation= deg_to_rad(180)
			$Yeast/flowarea.add_child(nt)


func _on_timer_timeout():
	var nf = newfluid.instantiate()
	nf.position = Vector2(150,-50)

	$Yeast/flowarea.add_child(nf)

	nf = newfluid.instantiate()
	nf.position = Vector2(120,-50)
	nf.get_node("ColorRect").color = Color(1,0,0)
	$Yeast/flowarea.add_child(nf)

#func _input(event):
	 ## Mouse in viewport coordinates
	#if event is InputEventMouseButton:
		#print("Mouse Click/Unclick at: ", event.position)
	#elif event is InputEventMouseMotion:
		#print("Mouse Motion at: ", event.position)
