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
programtitle="SimplePythonMenu"


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

# =======================
#    MENUS DEFINITIONS
# =======================

#Fill the options as needed.

def printMenu(menu):
	if(menu=="second"):
		print ("\033[45m       "+programtitle+"         	"+cc)
		print (colors["menu2c"]+" Second menu title			"+cc)
		print (colors["menu2c"]+" [1] Option 1				"+cc)
		print (colors["menu2c"]+" [2] Option 2				"+cc)
		print (colors["menu2c"]+" [3] Option 3				"+cc)
		print (colors["menu2c"]+" [4] Option 4				"+cc)
		print (colors["menu2c"]+" [q] Option 1b				"+cc)
		print (colors["menu2c"]+" [w] Option 2b				"+cc)
		print (colors["menu2c"]+" [e] Option 3b				"+cc)
		print (colors["menu2c"]+" [r] Option 4b				"+cc)
		print (colors["menu2c"]+" [t] Option 5b				"+cc)
		print (colors["menu2c"]+" [y] Option 6b				"+cc)
		print (colors["menu2c"]+" [9] Back (or press ENTER)		"+cc)
		print (colors["menu2c"]+" [0] Quit (or use CNTRL+C)		"+cc)
	else:#Main menu by default
		print ("\033[45m       "+programtitle+"        		"+cc)
		print (colors["menu1c"]+" Second menu title			"+cc)
		print (colors["menu1c"]+" [1] Option 1				"+cc)
		print (colors["menu1c"]+" [2] Option 2				"+cc)
		print (colors["menu1c"]+" [3] Option 3				"+cc)
		print (colors["menu1c"]+" [4] Option 4				"+cc)
		print (colors["menu1c"]+" [q] Option 1b				"+cc)
		print (colors["menu1c"]+" [w] Option 2b				"+cc)
		print (colors["menu1c"]+" [e] Option 3b				"+cc)
		print (colors["menu1c"]+" [r] Option 4b				"+cc)
		print (colors["menu1c"]+" [t] Option 5b				"+cc)
		print (colors["menu1c"]+" [y] Option 6b				"+cc)
		print (colors["menu1c"]+" [9] Back (or press ENTER)		"+cc)
		print (colors["menu1c"]+" [0] Quit (or use CNTRL+C)		"+cc)
		
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

# Back to main menu
def back():
	pass

# Exit program
def exit():
	sys.exit()
	
#Handles the CNTRL+C to leave properly the script
def sigint_handler(signum, frame):
	print("CNTRL+C exit")
	sys.exit(1)

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
        elif ch == 'q':
            pass
        elif ch == 'w':
            pass
        elif ch == 'e':
            pass
        elif ch == 'r':
            pass
        elif ch == 't':
            pass
        elif ch == 'y':
            pass
        elif (ch == '9') or (ch==''):
            back()
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
        elif ch == 'q':
            pass
        elif ch == 'w':
            pass
        elif ch == 'e':
            pass
        elif ch == 'r':
            pass
        elif ch == 't':
            pass
        elif ch == 'y':
            pass
        elif (ch == '9') or (ch==''):
            back()
        elif ch == '0':
            sys.exit()
        else:
            printError()

# =======================
#      MAIN PROGRAM
# =======================

def actuator(type,ch):
    if type == 0:
        menu=menu1()
        menu.action(ch)
    else:
        menu=menu2()
        menu.action(ch)
	
def main_menu():
	printMenu("main")
	choice = raw_input(" >> ")
	if(choice=="i"):
		printMenu("second")
		choice = raw_input(" >> ")
		actuator(1,choice)
	else:
		actuator(0,choice)
	
def main_loop():
	signal.signal(signal.SIGINT, sigint_handler)
	while True:
		main_menu()
		print("\n")

# Main Program
if __name__ == "__main__":
	main_loop()