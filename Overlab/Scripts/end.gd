extends Control

var team_name = ""
var score_list = {}
#var path = "res://GERF_version/savefile/save_score.s"
#var path = "res://GERF_version/savefile/save_score.text"

var path = "user://save_score.save"


func start():
	show()
	$Label2.text = "Score: " + str(GlobalVariableOverlab.score)
	
	if GlobalVariableOverlab.score < 300:
		$Label3.text = "Not Impressive"
	elif GlobalVariableOverlab.score > 900:
		$Label3.text = "Awesome TeamWork"
	else:
		$Label3.text = "Good Job!"	

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

func save_to_file(content,path):

	var file = FileAccess.open(path, FileAccess.WRITE)
	file.store_string(content)

func save_score(name,finalscore):
	#var name = "Rodrigo"
	#var finalscore = 10000
	var score_file = load_from_file(path)
	var content = score_file  + name + ":" + str(finalscore) + ";"
	save_to_file(content,path)
	GlobalVariableOverlab.score_content = content


func _on_button_pressed() -> void:
	save_score($LineEdit.text,GlobalVariableOverlab.score)
	get_tree().change_scene_to_file("res://Scenes/starting_menu.tscn") 


'func _on_line_edit_text_submitted(new_text: String) -> void:
	print("submit")


func _on_line_edit_text_changed(new_text: String) -> void:
	print("changed")'
