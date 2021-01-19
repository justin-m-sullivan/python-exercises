# This is my import_exercise solutions file

# 1. Import and test 3 of the functions from your functions exercise file.

#    Import each function in a different way:

#       >> import the module and refer to the function with the . syntax
import function_exercises

function_exercises.is_two(2)

#       >> use from to import the function directly
from function_exercises import calculate_tip

#       >> use from and give the function a different name
from function_exercises import apply_discount as discount

# For the following exercises, read about and use the itertools module from the standard library 
# to help you solve the problem.

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import combinations

from itertools import permutations

len(list(combinations("ABC123",3)))
# There are 20 different ways to combine abc with 123

# 2. How many different ways can you combine two of the letters from "abcd"?
len(list(permutations("abcd", 2)))
# There are 12 ways