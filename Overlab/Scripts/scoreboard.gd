extends VBoxContainer

#var path = "res://GERF_version/savefile/save_score.s"
var ori_path = "res://savefile/save_score.s"

var path = "user://save_score.save"
#var path = "res://GERF_version/savefile/save_score.text"

var score_list = {}



func _ready() -> void:
	#DirAccess.remove_absolute(path)
	#var file5 = FileAccess.open(path, FileAccess.WRITE)
	#print(OS.get_user_data_dir())
	write_scoreboard()	

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("reset"):
			reset_score()



func load_from_file(path):
	
	var file = FileAccess.open(path, FileAccess.READ)
	if file == null:
		var file2 = FileAccess.open(path, FileAccess.WRITE)
		file = FileAccess.open(ori_path, FileAccess.READ)
		file2.store_string(file.get_as_text())
	var content = file.get_as_text()
	#GlobalVariableOverlab.score_content = content
	return content


func load_score():
	score_list = {}
	var score = load_from_file(path)
	for i in score.count(";"):
		var line = score.split(";")[i]
		score_list[line.split(":")[0]] = int(line.split(":")[1])

func save_to_file(content,path):
	var file = FileAccess.open(path, FileAccess.WRITE)
	file.store_string(content)

func save_score(name,finalscore):
	#var name = "Rodrigo"
	#var finalscore = 10000
	var score_file = load_from_file(path)
	var content = score_file  + name + ":" + str(finalscore) + ";"
	save_to_file(content,path)


func reset_score():
	#var name = "Rodrigo"
	#var finalscore = 10000
	var score_file = load_from_file(path)
	var content = ""
	save_to_file(content,path)


func write_scoreboard():
	load_score()
	#sort them
	var sorted_list = sort_dict_by_value(score_list)
	
	var count = 1
	for n in sorted_list:
		if count < 11:
			get_node(str(count)).text = str(count) + ". " + n + ": " + str(sorted_list[n])
			count += 1
		else:
			return



func sort_dict_by_value(big_dict) -> Dictionary:
	#var big_dict := {}

	var items := []
	for key in big_dict.keys():
		items.append([key, big_dict[key]])

	items.sort_custom(func(a, b):
		return a[1] > b[1]
	)

	var sorted_dict = {}
	for item in items:
		sorted_dict[item[0]] = item[1]

	return sorted_dict
