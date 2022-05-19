#Hangman
import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
gallow = '''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
  ___|___
'''
print(gallow)

#choose the word
word_list = ["water", "baboon", "camel", "candy", "milk"]
chosen_word = random.choice(word_list)

#Generate the blanks


#Ask player to guess
guess = input("\nGuess a letter: ").lower()

#Check if guess is in chosen word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")



hangman = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
  ___|___
'''
