extends Node


var score = 0
var time = 80

var nplayer = 1
var player_ID = []
var playerskin = [0,0,0,0]

var score_content =""
var isfullscreen = false


var tuto_on = true

var tuto_item_player_hand = [0,0,0,0]
var tuto_step = 0



func init_var():
	nplayer = 0
	playerskin = [0,0,0,0]
	score = 0
