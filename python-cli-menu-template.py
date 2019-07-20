#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :Simple Python Menu
#description     :Template for a custom scripting menu
#author          :@cortesjorgea
#date            :10/2018
#version         :1.0
#usage           :simple_python_menu.py
#notes           :Change title in USER CONFIG. Create custom actions at BACKEND. Fill the actions in menu1 and menu2.
#python_version  :2.7.15  
#=======================================================================

# Import the modules needed
import sys, os, signal, colorama
colorama.init() #Color init for Windows

# =======================
#    USER CONFIG
# =======================
programtitle="SimplePythonMenu     "

# =======================
#    DEFINES
# =======================

colors={
	"info":     "35m",  	#Orange for info messages
	"error":    "31m",  	#Red for error messages
	"ok":       "32m",   	#Green for success messages
	"menu2c":	"\033[46m",	#Light blue menu
	"menu1c":	"\033[44m",	#Blue menu
	"close":	"\033[0m"	#Color coding close
	}
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]
# =======================
#    MENUS DEFINITIONS
# =======================

#Fill the options as needed.

def printMenu(menu):
	if(menu=="second"):
		print (ct+"       "+programtitle+"             "+cc)
		print (cs+" Second menu title                       "+cc)
		print (c2+" [1] Option 1                            "+cc)
		print (c2+" [2] Option 2                            "+cc)
		print (c2+" [3] Option 3                            "+cc)
		print (c2+" [4] Option 4                            "+cc)
		print (c2+" [5] Option 1b                           "+cc)
		print (c2+" [a] Option 2b                           "+cc)
		print (c2+" [s] Option 3b                           "+cc)
		print (c2+" [d] Option 4b                           "+cc)
		print (c2+" [e] Option 5b                           "+cc)
		print (c2+" [f] Option 6b                           "+cc)
		print (c2+" [9] Main menu                           "+cc)
		print (c2+" [0] Quit (or use CNTRL+C)               "+cc)
	else:#Main menu by default
		print (ct+"       "+programtitle+"             "+cc)
		print (cs+" Main menu title                         "+cc)
		print (c1+" [1] Option 1                            "+cc)
		print (c1+" [2] Option 2                            "+cc)
		print (c1+" [3] Option 3                            "+cc)
		print (c1+" [4] Option 4                            "+cc)
		print (c1+" [5] Option 1b                           "+cc)
		print (c1+" [a] Option 2b                           "+cc)
		print (c1+" [s] Option 3b                           "+cc)
		print (c1+" [d] Option 4b                           "+cc)
		print (c1+" [e] Option 5b                           "+cc)
		print (c1+" [f] Option 6b                           "+cc)
		print (c1+" [9] Second menu                         "+cc)
		print (c1+" [0] Quit (or use CNTRL+C)               "+cc)
		
# =======================
#      HELPERS
# =======================
def printWithColor(color,string):
	print("\033["+colors[color]+" "+string+cc)
def printError():
	printWithColor("error","Error!!")
	return 1
def printSuccess():
	printWithColor("ok","Success!!")
	return 0

# Exit program
def exit():
	sys.exit()
	
#Handles the CNTRL+C to leave properly the script
def sigint_handler(signum, frame):
	print("CNTRL+C exit")
	sys.exit(0)

# =======================
#      BACKEND
# =======================

#Create here custom actions.

# =======================
#      ACTIONS
# =======================

#First menu actions. Fill the actions for each selection.
class menu1():
	def action(self,ch):
		if   ch == '1':
			pass
		elif ch == '2':
			pass
		elif ch == '3':
			pass
		elif ch == '4':
			pass
		elif ch == '5':
			pass
		elif ch == 'a':
			pass
		elif ch == 's':
			pass
		elif ch == 'd':
			pass
		elif ch == 'e':
			pass
		elif ch == 'f':
			pass
		elif (ch==''):
			pass # Print menu again
		elif ch == '0':
			sys.exit()
		else:
			printError()

#Second menu actions. Fill the actions for each selection.
class menu2(menu1):
	def action(self,ch):
		if   ch == '1':
			pass
		elif ch == '2':
			pass
		elif ch == '3':
			pass
		elif ch == '4':
			pass
		elif ch == '5':
			pass
		elif ch == 'a':
			pass
		elif ch == 's':
			pass
		elif ch == 'd':
			pass
		elif ch == 'e':
			pass
		elif ch == 'f':
			pass
		elif (ch==''):
			pass # Print menu again
		elif ch == '0':
			sys.exit()
		else:
			printError()

# =======================
#      MAIN PROGRAM
# =======================

class main_menu:
	def __init__ (self):
		self.menu="main"
	
	def menuExecution(self):
		printMenu(self.menu)
		choice = raw_input(" >> ")
		if(self.menu=="main"):
			if(choice=="9"):
				self.menu="second"
			else:
				self.actuator(0,choice)
		else:
			if(choice=='9'):
				self.menu="main"
			else:
				self.actuator(1,choice)
		print("\n")
	
	def actuator(self,type,ch):
		if type == 0:
			menu=menu1()
			menu.action(ch)
		else:
			menu=menu2()
			menu.action(ch)


def main_loop():
	x = main_menu()
	signal.signal(signal.SIGINT, sigint_handler)
	while True:
		x.menuExecution()

# Main Program
if __name__ == "__main__":
	main_loop()