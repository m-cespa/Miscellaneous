# MorseCodeTranslator.py
#
#Script to translate from english to morse code & vice versa

# Defining english to morse dictionary
english_to_morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-' }

# Defining the reverse dictionary
morse_to_english_dict = {v:k for k,v in english_to_morse_dict.items()}

# english to morse encryption
def encrypt(messageE):
    morse = ''
    for letter in messageE:
        if letter != ' ':
            morse += english_to_morse_dict[letter] + ' '
# single spacing between morse letters
        else:
            morse += '  '
# double spacing between words
    return morse

# morse to english decryption where morse must be inputted
# with same spacing as the encryption syntax

# def decrypt(messageM):
#     english = morse_charac = ''
#     for letter in messageM:
#         if letter != ' ':
#             i = 0
#             morse_charac += letter
# # i stores number of spaces where 1 = new character, 2 = new word
#         else:
#             i += 1
# # add 1 to denote spacing for upcoming new morse character
#             if i == 2:
#                 english += ' '
#             else:
#                 english += morse_to_english_dict[morse_charac]
#                 morse_charac = ''
#     english += morse_to_english_dict[morse_charac]
# # if 2 consecutive spaces (new word), adds 1 space to english decryption         
#     return english

# alternatively using the .join() command
def decrypt(messageM):
    return "".join(\
        "".join(morse_to_english_dict[c] for c in word.split(" "))\
            for word in messageM.split("  "))

# selection for encryption or decryption
select = input("Type 'D' for decrypting morse or 'E' for encrypting english: ")
if select == 'D':
    messageM = input("Type your morse code (use single spacings between characters and double spacings between words): ")
    result = decrypt(messageM)
    print(result)
else:
    messageE = input("Type your english sentence (follow standard sentence syntax): ")
    result = encrypt(messageE)
    print(result)




