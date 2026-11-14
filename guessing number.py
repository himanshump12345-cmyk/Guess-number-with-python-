def main():
  import random 
  number=random.randint(1,30)
  while True:
      try:
         guess_1=int(input("what's your first guess "))
         print()
         
         if guess_1 <1 or guess_1 >30:
            print("Bro, please guess number from 1 to 30 🥀")
         else:
             break 
             
      except ValueError:
            print("Bro , please 🥺 guess a number")
        


  while True:
      try:
         guess_2=int(input("what's your second guess 🌚 "))
         print()
         if guess_2 <1 or guess_2 >30:
           print("Bro, please guess number from 1 to 30 🥀🥀")
           print()
         else:
             break 
      except ValueError:
            print("Bro, Do you have allergies with number if not then guess a number")
            print()
       
  while True:
      try:
         guess_3=int(input("what's your third and last guess 👽 "))
         print()
         print()
         if guess_3 <1 or guess_3 >30:
           print()
           print("Bro, please guess number from 1 to 30 🥀🥀🥀")
           print()
         else:
             break 
      except ValueError:
           print("Bruh , what are you even guessing 😐🥀")
           print()
       

  if guess_1==number:
    print("congratulations 🎉 , you won in first guess ")
    print()
    
  elif guess_2==number:
    print("congratulations 🎉, you won in your second guess ")
    print()
    
  elif guess_3==number:
    print("congratulations 🎉 , you won in your third guess ")
    print()
  else:
      print("you lose , even after three guess ")
      print()
  print("The number was ", number )

  choice=input("Do you want to play again? ").lower().strip()
  if choice=="yes":
       main()
  else:
      print("Thank you
 ")
main()

    
    
    
  