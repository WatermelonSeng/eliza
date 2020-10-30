answer = input("Is it your birthday today?")
if answer == "yes":
  print("Wow! Have a great celebration!")
elif answer == "no":
  answer2 = input("Is your birthday over?")
  if answer2 == "yes":
    print("Hope you had a great celebration!")
  elif answer2 == "no":
    print("I look forward to your celebration!")
  else:
    print("Please answer only yes or no.")
else:
  print("Please answer only yes or no.")
