extends VBoxContainer

var path = "res://GERF_version/savefile/save_score.s"
var score_list = {}
func _ready() -> void:
	reset_score()
	save_score("test1",10)
	save_score("test2",200)
	save_score("test3",50)
	save_score("test4",10000)

	write_scoreboard()	

func save_to_file(content,path):
	var file = FileAccess.open(path, FileAccess.WRITE)
	file.store_string(content)

func load_from_file(path):
	var file = FileAccess.open(path, FileAccess.READ)
	var content = file.get_as_text()
	return content


func load_score():
	score_list = {}
	var score = load_from_file(path)
	for i in score.count(";"):
		var line = score.split(";")[i]
		score_list[line.split(":")[0]] = int(line.split(":")[1])



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
