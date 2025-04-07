extends RigidBody2D


func PickUP(player):
	#player.add_child(self)
	if player.inventory == null:
		player.inventory = self


func Drop(player):
	if player.inventory != null:
		player.inventory = null
	#get_parent().get_parent().add_child(self)
