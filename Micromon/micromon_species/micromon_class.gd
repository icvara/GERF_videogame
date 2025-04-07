extends Node2D
class_name Micromon



var micromon_name = "none"
var HP = 100
var type = "none"

var skills = {
	"1":null,
	"2":null,
	"3":null,
	"4":null
}


func PickUp(player):
	for m in  player.micromon_inv:
		if player.micromon_inv[m] == null:
			player.micromon_inv[m] = self
			print("acquired " + player.micromon_inv[m].micromon_name + "!")
			hide()
			$CollisionShape2D.disabled = true
			get_parent().get_node("CanvasLayer").get_node("Inventory").updateTeam(player)
			#queue_free()
			return
	print("inventory full")
	return

func Drop(ID,player):
	player.micromon_inv[ID] = null
	position = player.position
	show()
	$CollisionShape2D.disabled = false

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
