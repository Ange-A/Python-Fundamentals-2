import pandas as pd

course= 'Python for Beginners'
len()
course.title()
course.find()
course.replace()
'...'in course

i= 1
while i <= 5:
  print(i)
  i = i + 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
       print("You won!")
       break
else:
    print("Keep trying!")
    
command = ""  
while command != "quit":
  command = input("> ").lower()
  if command == "start":
      print("Car started...")
  elif command == "stop":
      print("Car stopped.")
  elif command == "help":
     print("""
     start - to start the car
     stop - to stop the car
     quit - to quit
     """)
  else:
      print("Sorry, it makes no sense")

 
  
