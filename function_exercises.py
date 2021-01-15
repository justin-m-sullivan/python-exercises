# Functions Exercises
# Create a file named function_exercises.py for this exercise. 
#After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, 
# False otherwise.

# is_two defines a single parameter, num that is an int, and returns a boolean
def is_two(num):
    #check to see if the int input is 2
    return num == 2 or num == '2'

is_two(2)

# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel(v):
    return v in 'aeiouAEIOU'
    # "return string.lower() in 'aeiou' also works"

is_vowel(v)


# 3 Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(c):
    
    return c.isalpha() and not is_vowel(c)

 is_consonant()   
        
    

# 4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def user_word_input():
    user_word = input("Please enter a word: ")
    if user_word[0] not in ["a", "e", "i", "o", "u"]:
        return user_word.capitalize()
    else:
        return user_word


# 5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.


def calculate_tip():
    percentage_to_tip = float(input('Please enter the % you would like to tip as a decimal: '))
    bill_total = float(input('Please enter the total bill: '))
    
    amount_to_tip = bill_total * percentage_to_tip
    
    return f"The tip amount is: ${round(amount_to_tip,2)}"

    

# 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

# apply_dicount(item_price: float, discount: float) --> float
# apply_discount defines two parameters, a price of an item as a float and a discount % as a float, and it returns the value for the dicounted item price
def apply_discount():
    # sets the variable original_price by user input
    original_price = float(input('Please enter the original item price: '))

    discount_percentage = float(input('Please enter the discount as a decimal: '))
    
    discount_price = original_price - original_price * discount_percentage
    
    return f"The discounted price is: ${discount_price}"

# 7 Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.

# handle_commas accepts a single parameter, a number with a comma i.e. 1,000, and returns that input as an int without the commas
def handle_commas():
    user_num = input('Please enter a number with commas: ')
    # using the string methods int and .replace we remove the commas with an empty value, convert the string to an int and return that value 
    return float(user_num.replace(',','')) 

# 8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

# get_letter_grade defines a single parameter, a grade as an int, and returns the corresponding letter grade
def get_letter_grade():

    #set grade_as_num variable to user input and converts that input to int
    grade_as_num = int(input('Enter your grade as a number: '))
    
    #passes value through these conditional statements to determine corresponding letter grade and returns that grade
    if grade_as_num >= 90:
        return 'Your Grade is: A'
    elif grade_as_num >= 82:
        return 'Your Grade is: B'
    elif grade_as_num >= 76:
        return 'Your Grade is: C'
    elif grade_as_num >= 70:
        return 'Your Grade is: D'
    elif grade_as_num <70:
        return 'You Grade is: F'

# 9 Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.

# remove_vowels takes a single parameter, a string that is a word, 
# and returns that sting after removing any vowels
def remove_vowels():
    #accept a user input to define the word variable
    word = input('Please enter a word: ')
    for vowels in word:
        #ierate over characters in word to check for vowel membership
        if vowels in "aeiouAEIOU":
            #using .replace we replace vowels with an empty value
            word = word.replace(vowels,'')
    #returns word sans vowels 
    return word

# Shortcut solution:
# def remove_vowels(string): 
#   return "".join([c for c in string if not is_vowel(c)])


#10. Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
#   >> anything that is not a valid python identifier should be removed
#   >> leading and trailing whitespace should be removed
#   >> everything should be lowercase
#   >> spaces should be replaced with underscores
#   for example:
#       >> Name will become name
#       >> First Name will become first_name
#       >> % Completed will become completed

# normalize_name defines a single parameter, name that is a string, 
# and returns that string in python friendly format
def normalize_name():
    #create variable user_input from the input string on terminal
    user_input = input("Please enter your string: ")

    #begin iterating over sting to modify it in up to three ways:
    
    for char in user_input:
        #first modification replaces any whitespace with an underscore using .replace:
        user_input = user_input.replace(" ", "_") #this does no solve trailing or leading whitespace. See demo code below.
        for char in user_input:
            #second modification converts all characters to lowercase using .lower:
            user_input = user_input.lower()
            for char in user_input:
                #third modification ierates over string for  any invalid python identifiers 
                if char in "!@#$%^&*,>?/":
                    #using .replace with and empty value, we remove any invalid characters
                    user_input = user_input.replace(char,"")
    #the user_input string is returned, modified accordingly if any or all of the above modifications were necessary
    return user_input

#demo solution:
def normalize_name(s):
    valid_identifier = []
    for char in s:
        if char.isidentifier() or char == ' ':
            valid_identifier.append(character)
    valid_identifier = "".join(valid_identifier)
    valid_identifier = valid_identifier.lower()
    #this removes any trailing or leading whitespace
    valid_identifier = valid_identifier.strip()
    valid_identifier = valid_identifier.replace(' ', '_')
    return valid_identifier

#11. Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
# >> cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# >> cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# cumulative_sum defines the paramater to accept a string of numbers 
# and returns the cumulative sum of the inputs as a new list"'
def cumulative_sum():
    #import cumulative sum tool for iterating over the string input 
    from itertools import accumulate

    #asks for an input of numbers as a string
    user_nums = input("Please enter a list of numbers: ")

    #Here I modify the input string into a list of integers using the string method .split
    user_nums = [int(n) for n in user_nums.split(',')]

    #
    return list(accumulate(user_nums))

# demo solution with print statements:
def cumulative_sum(list_of_numbers):
    sums = [list_of_numbers[0]]
    print(f"sums: {sums}")
    for n in list_of_numbers[1:]:
        previous_total = sums[-1]
        sums.append(previous_total + n)
        print(f'End of for loop. sums: {sums}')
        return sums
