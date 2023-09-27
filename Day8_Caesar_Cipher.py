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