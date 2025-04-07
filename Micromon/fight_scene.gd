extends Control

@export var player: Node2D

# Called when the node enters the scene tree for the first time.
func _ready():
	#hide()
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass



func Start():
	show()
	update_micromon("Player", "1")
	
	
func update_micromon(battleID, InvID):
	get_node(battleID).get_node("Sprite")
	get_node(battleID).get_node("Label").text = player.micromon_inv[InvID].micromon_name
	
