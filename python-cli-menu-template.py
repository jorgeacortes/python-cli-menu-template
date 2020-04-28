#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :Simple Python Menu
#description     :Template for a custom scripting menu
#author          :@cortesjorgea
#date            :10/2018
#updated         :04/2020
#version         :2.0
#usage           :simple_python_menu.py
#notes           :Update section USER CONFIG dicts and reimplement methods
#                 of menu1 and menu2 classes at BACKEND section.
#python_version  :3.8.0
#=======================================================================
import sys, os, signal, colorama
colorama.init() # Color init for Windows

# =======================
#    DEFINES
# =======================

colors = {
  "info":     "35m",      #Orange for info messages
  "error":    "31m",      #Red for error messages
  "ok":       "32m",      #Green for success messages
  "menu2c":  "\033[46m",  #Light blue menu
  "menu1c":  "\033[44m",  #Blue menu
  "close":  "\033[0m"     #Color coding close
  }
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]


# =======================
#    USER CONFIG
# =======================
programtitle="SimplePythonMenu"

# Fill the options as needed.
menu2_colors = {
  "ct":ct,
  "cs":cs,
  "opt":c2
}
menu2_options = {
  "title":  "Second menu",
  "1":      "Option 1",
  "2":      "Option 2",
  "3":      "Option 3",
  "4":      "Option 4",
  "5":      "Option 5",
  "a":      "Option a",
  "s":      "Option s",
  "d":      "Option d",
  "e":      "Option e",
  "f":      "Option f",
  "9":      "Main menu",
  "0":      "Quit (or use CNTRL+C)",
}
menu1_colors = {
  "ct":ct,
  "cs":cs,
  "opt":c1
}
menu1_options = {
  "title":  "First menu",
  "1":      "Option 1",
  "2":      "Option 2",
  "3":      "Option 3",
  "4":      "Option 4",
  "5":      "Option 5",
  "a":      "Option a",
  "s":      "Option s",
  "d":      "Option d",
  "e":      "Option e",
  "f":      "Option f",
  "9":      "Second menu",
  "0":      "Quit (or use CNTRL+C)",
}

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
#      ACTIONS
# =======================

# Menu template
class menu_template():

  def __init__(self,options,colors):
    self.menu_width = 50  # Width in characters of the printed menu
    self.options = options
    self.colors = colors

# =======================
#      Menu prints
# =======================
  def createMenuLine(self,letter,color,length,text):
    menu = color+" ["+letter+"] "+text
    line = " "*(length-len(menu))
    return  menu+line+cc

  def createMenu(self,size):
    line = self.colors["ct"] + " "+programtitle
    line += " "*(size-len(programtitle)-6)
    line += cc
    print (line)  # Title
    line = self.colors["cs"] + " "+self.options["title"]
    line += " "*(size-len(self.options["title"])-6)
    line += cc
    print (line) # Subtitle
    for key in self.options:
      if(key != "title"):
        print (self.createMenuLine(key,self.colors["opt"],size,self.options[key]))

  def printMenu(self):
    self.createMenu(self.menu_width)
# =======================
#      Action calls
# =======================
  def action(self,ch):
    if   ch == '1':
      self.method_1()
    elif ch == '2':
      self.method_2()
    elif ch == '3':
      self.method_3()
    elif ch == '4':
      self.method_4()
    elif ch == '5':
      self.method_5()
    elif ch == 'a':
      self.method_a()
    elif ch == 's':
      self.method_s()
    elif ch == 'd':
      self.method_d()
    elif ch == 'e':
      self.method_e()
    elif ch == 'f':
      self.method_f()
    elif (ch==''):
      pass # Print menu again
    elif ch == '0':
      sys.exit()
    else:
      printError()
# =======================
#      Empty methods
# =======================
  def method_1(self):
    pass
  def method_2(self):
    pass
  def method_3(self):
    pass
  def method_4(self):
    pass
  def method_5(self):
    pass
  def method_a(self):
    pass
  def method_s(self):
    pass
  def method_d(self):
    pass
  def method_e(self):
    pass
  def method_f(self):
    pass


# =======================
#      BACKEND
# =======================

# Create here custom actions.

# First menu actions. Implement each method.
class menu1(menu_template):
  pass

# Second menu actions. Implement each method.
class menu2(menu_template):
  pass

# =======================
#      MAIN PROGRAM
# =======================

class menu_handler:

  def __init__ (self):
    self.current_menu="main"
    self.m1=menu1(menu1_options, menu1_colors)
    self.m2=menu2(menu2_options, menu2_colors)

  def menuExecution(self):
    if(self.current_menu=="main"):
      self.m1.printMenu()
    else:
      self.m2.printMenu()
    choice = input(" >> ")
    if(self.current_menu=="main"):
      if(choice=="9"):
        self.current_menu="second"
      else:
        self.actuator(0,choice)
    else:
      if(choice=='9'):
        self.current_menu="main"
      else:
        self.actuator(1,choice)
    print("\n")

  def actuator(self,type,ch):
    if type == 0:
      self.m1.action(ch)
    else:
      self.m2.action(ch)

# Main Program
if __name__ == "__main__":
  x = menu_handler()
  signal.signal(signal.SIGINT, sigint_handler)
  while True:
    x.menuExecution()
