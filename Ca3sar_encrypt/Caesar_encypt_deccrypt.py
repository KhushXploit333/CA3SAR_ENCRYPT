letters = 'abcdefghijklmnopqrstuvwxyz' #index value as per caesar cipher algorithm
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >=num_letters:
                    new_index -= num_letters
                ciphertext += letters [new_index]
    return ciphertext
                


def dencrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
               plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                   new_index += num_letters
                plaintext += letters [new_index]
    return plaintext
                    






print()
print( '_____CAESAR CIPHER E/D______') # Programm tittle
print()

print("DO YOU WANT TO ENCRYPT OD DECRYPT?") # asking for what you want to choose 
user_input =input ('E/D:').lower() #Taking user input value e or d
print()

if user_input == 'e': # e stands for encryption as per algorithm for cipher
    print('ENCRYPTION MODE SELECTED') # mode select by user input
    print()
    key = int(input('Enter the key (1 through 26 : ')) # calculating the shift key as per caesar cipher algorithm 1 to 26 alphabetic letters
    text = input('Enter the text to encrypt :') 
    ciphertext = encrypt(text, key) # take a user input for plaintext into cipher (encryption)
    print(f'CIPHERTEXT : {ciphertext}') #showing the output value

elif user_input == 'd':  # d stands for dencryption as per algorithm for plaintxt
    print('DECRYPTION MODE SELECTED') # mode select by user input
    print()
    key = int(input('Enter the key (1 through 26 : '))
    text = input('Enter the text to dencrypt :')
    plaintext = dencrypt(text, key)  # take a user input for ciphertxt into plaintx (encryption)
    print(f'PLAINTEXT : {plaintext}') #showing the output value





              