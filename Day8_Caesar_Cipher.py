logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
more_cipher = True
while more_cipher: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
    ENCODE = "encode"
    DECODE = "decode"

    def shift_n_times(letter, n, direction): 
        if 'a'<=letter<='z':
            if direction == ENCODE:
                return alphabet[(alphabet.index(letter)+n) % 26]
            else:
                return alphabet[(alphabet.index(letter)-n) % 26]
        return  letter

    def encrypt(text, shift):
        encoded_text = ""
        for letter in text:
            encoded_text = encoded_text + shift_n_times(letter, shift, ENCODE)
        print("\nThe encoded text is:", encoded_text)

    def decrypt(text, shift):
        decoded_text = ""
        for letter in text:
            decoded_text = decoded_text + shift_n_times(letter, shift, DECODE)
        print("\nThe decoded text is:", decoded_text)

    if direction == ENCODE:
        encrypt(text, shift)
    elif direction == DECODE:
        decrypt(text, shift)
    else:
        print("\nWrong choice entered.")
        
    more_cipher = "yes" == input("\nEnter 'yes' to continue or 'no' to stop: ")
    print()
