extends Item


func _ready():
	item_ID = "DNA"




func _physics_process(delta: float) -> void:
	if player_holding:
		pass#apply_central_impulse(player_holding.velocity)

'func _process(delta: float) -> void:
	if player_holding:
		position = player_holding.position'
