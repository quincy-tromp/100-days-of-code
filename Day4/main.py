#Rock, paper, scissors
import random

play = True
while play == True:
    choices = ["Rock", "Paper", "Scissor"]
    results = ["Win", "Lose", "Draw"]

    rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
    paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        ''')
    scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        ''')

    hand_gestures = [rock, paper, scissor]

    your_choice = int(input('\nWhat do you choose?' + ' ' +
    f'Type "0" for Rock, "1" for Paper or "2" for Scissor.\n'))
    print(f"\nYou chose: {choices[your_choice]}\n" + 
    hand_gestures[your_choice])

    computer_choice = random.randint(0, len(choices)-1)
    print(f"\nComputer chose: {choices[computer_choice]}\n" + 
    hand_gestures[computer_choice])

    if your_choice == computer_choice:
        print(f"It's a Draw.")
    else:
        if (your_choice == "Rock" and computer_choice == "Scissor") \
        or (your_choice == "Paper" and computer_choice == "Rock") \
        or (your_choice == "Scissor" and computer_choice == "Paper"):
            print(f"You Win!")
        else:
            print(f"You Lose.")
    
    play_again = input('\nType "n" if you want to stop the program.\n').lower()
    if play_again == "n":
        play = False
        print("Goodbye.\n")