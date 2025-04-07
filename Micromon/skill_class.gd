#extends Node
class_name Skill



var name = "default"
var SP = 0
var attack = 0
var type = "neutre"



func Play(target):
	print("skill " + name + " played!")
	target.HP += 10
	target.HP = min(100, target.HP)
