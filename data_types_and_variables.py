## Python Data Types, Operators, and Variables Exercises

-- Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

 
# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
total_rent_cost = 0.00
rent_cost_per_day = 3.00
little_mermaid_days()
brother_bear_days()
hercules_days()

total_rental_cost = rent_cost_per_day * (little_mermaid_days + brother_bear_days + hercules_days)

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_hrly_rate = 400.00
amazon_hrly_rate = 380.00
fb_hrly_rate = 350.00
x = 6
y = 4
z = 10

weekly_pay_stub = (google_hrly_rate * x) + (amazon_hrly_rate * y) + (fb_hrly_rate * z)

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
is_class_full = True
no_schedule_conflict = True
student_can_enroll =  is_class_full and no_schedule_conflict
print(student_can_enroll)

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
two_items_or_more = True
offer_not_expired = True
is_premium_member = True

discount_applies = offer_not_expired and (two_items_or_more or is_premium_member)

print(discount_applies)

/* Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions: */

len(password) >= 5 and len(username) <= 20 and username != password and (username[0] != ' ' and password[0] != ' ')

# a. the password must be at least 5 characters

len(password) >= 5

# b. the username must be no more than 20 characters
len(usename) <= 20

# c. the password must not be the same as the username

username != password

# d. bonus neither the username or password can start or end with whitespace
username[0] != ' ' and password[0] != ' '
