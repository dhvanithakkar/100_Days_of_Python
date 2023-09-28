#i went a bit crazy here. Enforce complexity lol

import random
def generate_password(length, no_of_special_characters, no_of_numbers, complexity):
    lower_case_characters = [_ for _ in "abcdefghijklmnopqrstuvwxyz"]
    upper_case_characters = [_ for _ in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    digits = [_ for _ in "0123456789"]
    special_characters = [_ for _ in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''']

    all_characters = lower_case_characters + upper_case_characters

    length = max(8, length)
    password = ''.join(random.choice(all_characters) for _ in range(length-no_of_numbers-no_of_special_characters))
    special_characters_in_password = ''.join(random.choice(special_characters) for _ in range(no_of_special_characters))
    numbers_in_password = ''.join(random.choice(digits) for _ in range(no_of_numbers))
    password = random.shuffle(password + numbers_in_password + special_characters_in_password)
    if complexity:
        while True:
            is_complex = [False, False, False, False]
            for character in password:
                if character in lower_case_characters:
                    is_complex[0] = True
                if character in upper_case_characters:
                    is_complex[1] = True
                if character in digits:
                    is_complex[2] = True
                if character in special_characters:
                    is_complex[3] = True

            if use_special_characters and is_complex[0] and is_complex[1] and is_complex[2] and is_complex[3]:
                return password
            elif is_complex[0] and is_complex[1] and is_complex[2] and not use_special_characters:
                return password
            password = ''.join(random.choice(all_characters) for _ in range(length))
    else:
        return password

print("Welcome to the PyPassword Generator!")
length = int(input("Enter the desired password length (atleast 8 recommended): "))
no_of_special_characters = int(input("Enter number of special characters: "))
no_of_numbers = int(input(f"How many numbers would you like?: "))

if no_of_special_characters+no_of_numbers > length:
    print("Error. Number of special characters and digits cannot be greater than passowrd length.")
elif no_of_special_characters+no_of_numbers == length:
    print("Error. There needs to be atleast one letter.")
else:
    complexity = input("Enforce Complexity? (yes/no): ")[0].lower() == "y"
    password = generate_password(length, no_of_special_characters, no_of_numbers, complexity)
    print("Generated Password:", password)
