rock = ''' 

    _______ 

---'   ____) 

      (_____) 

      (_____) 

      (____) 

---.__(___) 

''' 

  

paper = ''' 

    _______ 

---'   ____)____ 

          ______) 

          _______) 

         _______) 

---.__________) 

''' 

  

scissors = ''' 

    _______ 

---'   ____)____ 

          ______) 

       __________) 

      (____) 

---.__(___) 

''' 

  

#Write your code below this line 👇 

game_images = [ rock, paper, scissors ] 

  

your_choice = int(input("Chose 0 : Rock, 1 : Paper, 2 : Scissors \n")) 

print(f"You chose\n {game_images[your_choice]}") 

#print(type(your_choice)) 

# if your_choice == 0: 

#   print(rock) 

# if your_choice == 1: 

#   print(paper) 

# if your_choice == 2: 

#   print(scissors) 

  

#play game further only if your choice is valid 

if your_choice > 2: 

  print("Invalid choice.") 

else: 

  import random 

  computer_choice = random.randint(0,2) 

  #print(type(computer_choice)) 

  print(f"Computer chose\n {game_images[computer_choice]}") 

  # if computer_choice == 0: 

  #   print(rock) 

  # if computer_choice == 1: 

  #   print(paper) 

  # if computer_choice == 2: 

  #   print(scissors) 

   

  #Winning conditions 

  if (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1) : 

    print("You win!") 

  elif your_choice == computer_choice: 

    print("It's a draw.") 

  else: 

    print("You lose.") 

  

 
