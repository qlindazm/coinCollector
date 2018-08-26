# coding: utf-8
# device: Mi8SE
# screen: 2244x1080
# adb support
# open USB debugging and allow simulating input via USB debugging
import os
import time

fir_in_button_x, fir_in_button_y = 1485, 870  # first button, click to start
check_in_button_x, check_in_button_y = 1400, 750   # dialog：英雄不足三个是否继续
time_waiting = 13   # loading time (second)
skip_x, skip_y = 2060, 65      # skip useless story
direc_x1, direc_y1, direc_x2, direc_y2 = 900, 364, 995, 485  # two mark points, calculate the direction 
direc_tan = (direc_y2 - direc_y1) / (direc_x2 - direc_x1)
magic_num1 = 35      # magic number to fix the direction so that you can walking straight
move_x, move_y = 450, 850    # the center of the left joystick
time_move1 = 32000     # time from the very begining to the boss, fixing according to your own moving speed (millisecond)
ult_ability_x, ult_ability_y = 1860, 620   # the position of the ultimate ability joystick(就是大招，反正之前打dota大招叫ultimate ability)
sec_ability_x, sec_ability_y = 1650, 750   # second ability 
A_x, A_y = 1850, 900      # basic attack
again_x, again_y = 1800, 980    # button(再次挑战)

while(True):
	os.system('adb shell input swipe {} {} {} {} {}'.format(fir_in_button_x, fir_in_button_y, fir_in_button_x, fir_in_button_y, 10)) # start the game (see: 1.png)
	os.system('adb shell input swipe {} {} {} {} {}'.format(check_in_button_x, check_in_button_y, check_in_button_x, check_in_button_y, 10))  # check dialog (see: 2.png)
	time.sleep(time_waiting)  # wait for loading
	os.system('adb shell input swipe {} {} {} {} {}'.format(skip_x, skip_y, skip_x, skip_y, 10))     # skip story
	print('move')
	os.system('adb shell input swipe {} {} {} {} {}'.format(move_x, move_y, move_x-50, move_y-50*direc_tan-magic_num1, time_move1)) # move to the boss
	print('attack')
	os.system('adb shell input swipe {} {} {} {} {}'.format(ult_ability_x, ult_ability_y, ult_ability_x, ult_ability_y, 3)) # ultimate ability
	os.system('adb shell input swipe {} {} {} {} {}'.format(sec_ability_x, sec_ability_y, sec_ability_x, sec_ability_y, 3)) # second ability
	print('A')
	for i in range(40):
		os.system('adb shell input swipe {} {} {} {} {}'.format(A_x, A_y, A_x, A_y, 1))   # basic attack and skip following story
	print('done')
	os.system('adb shell input swipe {} {} {} {} {}'.format(again_x, again_y, again_x, again_y, 10))  # play again?
	time.sleep(3)