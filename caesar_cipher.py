from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

end = False


print(logo)
def encrypt(text,shift):

    i=0
    for letter in text:
        if letter == " ":
            text[i] = " "
            i+=1

        elif letter.isupper():
            index = alphabet_caps.index(letter)
            cipher_position = (index+shift)%26
            text[i] = alphabet_caps[cipher_position]
            i+=1

        else:
            index = alphabet.index(letter)
            cipher_position = (index+shift)%26
            text[i] = alphabet[cipher_position]
            i+=1

    print(f"The encoded text is {''.join(text)} ")

def decrypt(text,shift):

    i=0
    for letter in text:
        if letter == " ":
            text[i] = " "
            i+=1

        elif letter.isupper():
            index = alphabet_caps.index(letter)
            plain_position = index-shift
            text[i] = alphabet_caps[plain_position]
            i+=1

        else:
            index = alphabet.index(letter)
            plain_position = index-shift
            text[i] = alphabet[plain_position]
            i+=1

    print(f"The decoded text is {''.join(text)} ")

while not end:
    option = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = list(input("Type your message:\n"))

    shift = int(input("Type the shift number:\n"))

    if option == "e":
        encrypt(text,shift)
    elif option == "d":
        decrypt(text,shift)
    else:
        print("Invalid option")
    restart = input("Wanna restart? (y/n) ").lower()
    if restart == "n":
        end = True




