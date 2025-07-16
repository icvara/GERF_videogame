extends Control


var mappings_key = {}


func _ready() -> void:
	default_mappings()
	for i in range(0,3):
		for k in $"Panel".get_node(str(i)).get_node("keyboard").get_children():
			k.text = mappings_key[k.name+str(i)]

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_up"):
		$Selector.position.y -= 10
	if Input.is_action_just_pressed("ui_down"):
		$Selector.position.y += 10
	if Input.is_action_just_pressed("ui_right"):
		$Selector.position.x += 10
	if Input.is_action_just_pressed("ui_left"):
		$Selector.position.x -= 10
		
'func _input(ev):
	if ev is InputEventKey :
		(print(ev.as_text_keycode() ))'

func default_mappings():
	var i =0
	mappings_key["down"+str(i)]= "S"
	mappings_key["up"+str(i)]= "W"
	mappings_key["right"+str(i)]= "D"
	mappings_key["left"+str(i)]= "A"
	mappings_key["space"+str(i)]= "SPACE"
	i =1
	mappings_key["down"+str(i)]= "K"
	mappings_key["up"+str(i)]= "I"
	mappings_key["right"+str(i)]= "L"
	mappings_key["left"+str(i)]= "J"
	mappings_key["space"+str(i)]= "#"
	i =2
	mappings_key["down"+str(i)]= "DOWN"
	mappings_key["up"+str(i)]= "UP"
	mappings_key["right"+str(i)]= "RIGHT"
	mappings_key["left"+str(i)]= "LEFT"
	mappings_key["space"+str(i)]= "SHIFT"
func map_new_key(ID):
	print (InputEventKey.keycode)
