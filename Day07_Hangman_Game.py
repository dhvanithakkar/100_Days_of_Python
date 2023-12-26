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

def list_to_string(li: list)-> str:
    s = ""
    for elem in li:
        s = s + str(elem)
    return s

hangman_graphics = [
    '''
      _______
     |/      |
     |    
     |       
     |       
     |     
     |
    _|___
    ''','''
      _______
     |/      |
     |      (_)
     |      
     |     
     |
     |
    _|___
    ''','''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |     
     |
    _|___
    ''','''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    '''
    
]


word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

import random
chosen_word = random.choice(word_list)

print(f"Solution is: {chosen_word}")

word_guessed = ["_"] * len(chosen_word)
wrong_guesses = 0

print(hangman_graphics[wrong_guesses])

while wrong_guesses < len(hangman_graphics) - 1 and list_to_string(word_guessed) != chosen_word:
    guess = input("Guess a Letter: ")[0].lower()
    match_with_chosen_word = []
    for letter in chosen_word:
        match_with_chosen_word.append(guess == letter)

    if not any(match_with_chosen_word):
        wrong_guesses += 1
        print("Guessed letter is not in the word.\n")
    
    elif guess in word_guessed:
        print("You have already guessed this letter.\n")

    else:
        for (index, match) in enumerate(match_with_chosen_word):
            if match:
                word_guessed[index] = guess
            
    print("Word guessed is:", end = " ")
    for l in word_guessed:
        print(l, end =" ")
    

    print(hangman_graphics[wrong_guesses])

if wrong_guesses == len(hangman_graphics) - 1:
    print("You Lose.")
    print("The correct word was", chosen_word)
else:
        print("You Win!")