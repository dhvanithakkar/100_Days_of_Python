############DEBUGGING#####################
def my_function() -> None:
    for i in range(1, 21):
        # for i in range(1, 20):
        # this will NOT reach 20 as last limit not included.
        # We want to print at i=20 so i let it reach 20.
        if i == 20:
            print("You got it")


my_function()

# # Reproduce the Bug
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num-1])#print(dice_images[dice_num]) indices are 0-5 not 1-6 as we want. so -1


# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:#1994 ke liye let it be gen z
#   print("You are a Gen Z.")
# else: print("You are neither Gen Z, nor a Millenial.")#added this else statement.

# # Fix the Errors
# age = int(input("How old are you? "))#age = input("How old are you? ") won't let us compare int with str so converted age to int
# if age >= 18:#if age > 18, >=18 makes more sense to me.
#     print(f"You can drive at age {age}.")#print("You can drive at age {age}.") without indentation. Fixed indentation and made it a formatted string to print variable age
# else: print(f"You cannot drive at age {age}.")#added else statement.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))#there was == here instead of = and needed print statements.
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger: Visualise on pythontutor.com it is legit great!!!
# def mutate(a_list): So many bugs baap re
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,5,8,13])
