from characters import alphabet

def caesar_cipher(direction, text, shift):
    cipher = ""
    shift = shift % 26
    if direction == "decode": 
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher += alphabet[new_position]
        else:
            cipher += char
    print(f"The {direction}d text is: {cipher}")