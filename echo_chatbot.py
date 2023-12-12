print("Bot: Welcome! How are you?")
print("Bot: This is a bot that echo's (repeat's) whatever you say!")
while(True):
  stuff_to_echo=input("Enter: ")
  print("You said: "+stuff_to_echo)
  if stuff_to_echo=="quit":
    print("Bot: Thank you!")
    break