extends Workstation

func _ready():
	size = Vector2(2,1)

func Use(player):
	if player.inventory:
		if player.inventory.item_ID == "Bioproduct":
				player.inventory.queue_free()
				GlobalVariableOverlab.score += 100
				displaytext("+100 points")
