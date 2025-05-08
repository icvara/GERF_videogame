extends Node2D

@export var transform_tile: PackedScene
@export var feed_tile: PackedScene
@export var block_tile: PackedScene
@export var move_tile: PackedScene

@export var newfluid: PackedScene

var cell_flow_size = Vector2(160,96)#$Yeast/flowarea.
var flow_tile_size = Vector2(16,16) #need to match the value in tile scene + script

var flowgrid = [[]] # 2D matrix

# Called when the node enters the scene tree for the first time.
func _ready():
	init_grid()
	#fill_the_cell()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	change_cell_face()


func init_grid():
	var grid_width = cell_flow_size.x / flow_tile_size.x
	var grid_height = cell_flow_size.y / flow_tile_size.y
	for i in grid_width:
		flowgrid.append([])
		for j in grid_height:
			flowgrid[i].append(0)
			#spawn_tile(Vector2(i,j),0)


'func fill_the_cell():
	var n_tile = cell_flow_size/16/2
	for i in n_tile.x:
		for j in n_tile.y:
			var nt = newtile.instantiate()
			nt.position = Vector2(i*16*2,j*16*2) 
			#if randi_range(0, 1) == 1:		
				#nt.get_node("StaticBody2D").rotation= deg_to_rad(180)
			$Yeast/flowarea.add_child(nt)'

func spawn_food(pos, col):
	


	var nf = newfluid.instantiate()
	nf.global_position = pos - $Yeast.position - $Yeast/flowarea.position - Vector2(2,2)
	nf.get_node("ColorRect").color = col
	$Yeast/flowarea.add_child(nf)

func spawn_tile(pos,type):
	var nt
	if type == 0:
		nt = transform_tile.instantiate()
	if type == 1:
		nt = feed_tile.instantiate()
	if type == 2:
		nt = block_tile.instantiate()
	if type == 3:
		nt = move_tile.instantiate()
	if nt:
		nt.position = pos * flow_tile_size 
		nt.isDragged = true
		$Yeast/flowarea.add_child(nt)

func _on_timer_timeout():
	
	'var nf = newfluid.instantiate()
	nf.position = Vector2(5*16-10,-50)
	$Yeast/flowarea.add_child(nf)'

	var nf = newfluid.instantiate()
	nf.position = Vector2(160-10-16,-50)
	nf.get_node("ColorRect").color = Color(1,0,0)
	$Yeast/flowarea.add_child(nf)
	
	
	nf = newfluid.instantiate()
	nf.position = Vector2(6,-50)
	nf.get_node("ColorRect").color = Color(0,1,0)
	$Yeast/flowarea.add_child(nf)
	
	$Yeast/HealthBar.value = clamp($Yeast/HealthBar.value - 5 ,0,100)

func change_cell_face():
	if $Yeast/HealthBar.value >= 100:
		$Yeast/yeastFace.text = ": 0"
	elif $Yeast/HealthBar.value >= 50 and $Yeast/HealthBar.value  < 100:
		$Yeast/yeastFace.text = "=)"
	elif $Yeast/HealthBar.value < 50 and $Yeast/HealthBar.value > 0:
		$Yeast/yeastFace.text = "=("
	elif $Yeast/HealthBar.value <= 0:
		$Yeast/yeastFace.text = "X ("

func _input(event):
		if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
			if event.pressed:
				pass
				#$Yeast/HealthBar.value -= 20	
				#spawn_food(event.position, Color(0,1,0))			


		if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_RIGHT:
			if event.pressed:
				#$Yeast/HealthBar.value -= 20
				pass

	
	 ## Mouse in viewport coordinates
	#if event is InputEventMouseButton:
		#print("Mouse Click/Unclick at: ", event.position)
	#elif event is InputEventMouseMotion:
		#print("Mouse Motion at: ", event.position)


func _on__pressed() -> void:
	spawn_tile(Vector2(11,0),0)

func _on_1_pressed() -> void:
	spawn_tile(Vector2(11,3),1)

func _on_2_pressed() -> void:
	spawn_tile(Vector2(11,1),2)


func _on_4_pressed() -> void:
	spawn_tile(Vector2(11,4),3)
