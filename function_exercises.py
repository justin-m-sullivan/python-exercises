# Functions Exercises
'''Create a file named function_exercises.py for this exercise. 
After creating each function specified below, write the necessary code in order to test your function.'''

# 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, 
# False otherwise.

def is_two(num):
    return num == 2

is_two(2)

# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel():
    string = input('Please enter a vowel: ')
    return string in ["a", "e", "i", "o", "u"]

is_vowel()


# 3 Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant():
    string = input('Please enter a consonant: ')
    if string not in is_vowel:
        return is_consonant

 is_consonant()   
        
    

# 4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def user_word_input():
    user_word = input("Please enter a word: ")
    if user_word[0] not in ["a", "e", "i", "o", "u"]:
        return user_word.upper()
    else:
        return user_word


# 5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip():
    percentage_to_tip = float(input('Please enter the % you would like to tip as a decimal: '))
    bill_total = float(input('Please enter the total bill: '))
    
    amount_to_tip = bill_total * percentage_to_tip
    
    return f"The tip amount is: ${amount_to_tip}"

    

# 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount():
    original_price = float(input('Please enter the original item price: '))
    discount_percentage = float(input('Please enter the discount as a decimal: '))
    
    discount_price = original_price - original_price * discount_percentage
    
    return f"The discounted price is: ${discount_price}"

# 7 Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.
def handle_commas():
    user_num = input('Please enter a number with commas: ')
    return int(user_num.replace(',','')) 

# 8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade():
    grade_as_num = int(input('Enter your grade as a number: '))
    
    if grade_as_num >= 90:
        return 'Your Grade is: A'
    if grade_as_num >= 82:
        return 'Your Grade is: B'
    if grade_as_num >= 76:
        return 'Your Grade is: C'
    if grade_as_num >= 70:
        return 'Your Grade is: D'
    if grade_as_num <70:
        return 'You Grade is: F'

Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.