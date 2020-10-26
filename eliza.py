from random import *
import math
ask='is something troubling you?'
while True:
  answer=input(ask)
  if answer == "yes":
    print("You can always seek a trusted adult for help, you know."
  elif answer == "no":
    print("Well, that's awesome!")
  else:
    print("Please answer only yes or no, or else no feedback can be given.")
