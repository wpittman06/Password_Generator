import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters #Creates a string with all the characters we have to select from
    if numbers: # if variable is true take digits and add them to letter string to combine
        characters += digits
    if special_characters: # if we have special characters we add them to letter string
        characters += special
   
# Loop iteration to generate new character to add to random password until criteria is met
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    '''
    While we are not meeting criteria or the length of password not yet equal to 
    or greater than minimal length continue to add characters until criteria met
    '''
    while not meet_criteria or len(pwd) < min_length: 
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # updates meet_criteria
        if numbers:
            meet_criteria = has_number
        if special_characters:
                meet_criteria = meet_criteria and has_special

    '''
    If we include a number then set the number equal to if we have a number or not, THEN if we have special characters meet_criteria is equal meet criteria and has_special.
    '''

    return pwd

min_length = int(input("Enter minimum length password: ")) 
# We ask user for length of desired password and then convert into integer
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
# We ask user if they want to include numbers and then checeks for a "y" value and assigns one if true.
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
# We ask user if they want to include special characters and then checks for a "y" value and assigns one if true.
pwd = generate_password(min_length, has_number, has_special)
print("The generated password id:", pwd)