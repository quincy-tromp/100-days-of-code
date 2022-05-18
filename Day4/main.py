#Rock, paper, scissors
import random

play = True
while play == True:
    choices = ["Rock", "Paper", "Scissor"]
    results = ["Win", "Lose", "Draw"]
    hand_gestures = [rock, paper, scissor]

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

    your_choice = int(input('\nWhat do you choose?' + ' ' +
    f'Type "0" for Rock, "1" for Paper or "2" for Scissor.\n'))
    print(f"\nYou chose: {choices[your_choice]}\n" + 
    hand_gestures[your_choice])

    computer_choice = random.randint(0, len(choices)-1)
    print(f"\nComputer chose: {choices[computer_choice]}\n" + 
    hand_gestures[computer_choice])

    if your_choice == computer_choice:
        result = "It's a Draw."
    else:
        if (your_choice == 0 and computer_choice == 2) \
        or (your_choice == 1 and computer_choice == 0) \
        or (your_choice == 2 and computer_choice == 1):
            result = "You Win!"
        else:
            result = "You Lose."
    print(result)
    
    play_again = input('\nDo you want to continue? (y/n): \n').lower()
    if play_again == "n":
        play = False
        print("Goodbye.\n")