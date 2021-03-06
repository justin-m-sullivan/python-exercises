## 1. Conditional Basics

>> a. prompt the user for a day of the week, print out whether the day is Monday or not

```
day_of_week = input("What is the day of the week? ")

if day_of_week == "Monday":
    print("Today is Monday")
else: 
    print("Today is not Monday")
```
# Alternatvely, the following code works as well:
```
if day_of_week.startswith("Mon"):
    print("Today is Monday")
```

>> b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input("What is the day of the week? ")

if day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Today is a weekday")
else: 
    print("Today is a weekend")

# Alt code solution from demo:
```
if day_of_week.lower().startswith('s'):
    print('Today is a weekend ')
```

>> c. create variables and make up values for

>> the number of hours worked in one week

``` 
hrs_worked = 40
```
>> the hourly rate
```
hrly_rate = 15.00
```
>> how much the week's paycheck will be
```
paycheck_amt = hrs_worked * hrly_rate

>> write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

``` 
hrly_rate = input("What is your hourly rate? ")
hrs_worked = input("How many hours did you work this week? ")
hrs_worked = float(hrs_worked)
hrly_rate = float(hrly_rate)

if hrs_worked > 40:
    overtime_hrs = hrs_worked - 40
else:
    overtime_hrs = 0

paycheck_amt = (hrly_rate) * (hrs_worked - overtime_hrs) + overtime_hrs * (hrly_rate * 1.5)
print("Your weekly paycheck will be: $",paycheck_amt)```
    



## 2. Loop Basics

>> a. While

>> Create an integer variable i with a value of 5.

i = 5

>> Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    i = i + 1 

>> Each loop iteration, output the current value of i, then increment i by one.
>>Your output should look like this:

"
5
6
7
8
9
10
11
12
13
14
15
"
>> Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

y = 2

while y in range(101):
    print(y)
    y = y + 2

>> Alter your loop to count backwards by 5's from 100 to -10.

y = 100
while y in range(-10,101):
    print(y)
    y = y - 5

>> Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

n = 2
while n ** 2 < 1_000_000:
    print(n)
    n = n ** 2
    >> shorthand operator for the above line of code is n *= n
 2
 4  
 16
 256
 65536

>> Write a loop that uses print to create the output shown below.

z = 100
while z >= 5:
    print(z)
    z = z - 5

100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5

>> b. For Loops

>> i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

x = input("Enter a number: ") 
x = int(x)

y = 1

while y < 11:
    print(f'{x}', 'x', f'{y}', '=', x * y)
    y = y + 1



>> For example, if the user enters 7, your program should output:

"
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"

>> Create a for loop that uses print to create the output shown below.

j = 1
for j in range(1,10):
    k = str(j)
    print(j,f'{k}' * j)
    
   
    
1
22
333
4444
55555
666666
7777777
88888888
999999999

>> c. break and continue

>> i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
def is_odd(x):
    x = input("Enter an odd number between 1 and 50: ")
    for x in x: 
        if x.isdigit():
            break
        else:
            return is_odd(x)

is_odd(x)   
       
for is_x in range(1,50):
    if x % 2 != 0:
        print(f'Here is an odd number: {x}')

 >> Solution from demo
 ```
while True: 
    user_number = int(input('Enter an odd number between 1 and 50'))
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number % 2 == 0:
            continue
        break

 i = 1
 while i <= 50:
     if i == user_number:
         print(f"Yikes! Skipping this number: {i}")
         i += 2
         continue
    print(f"Here is an odd number:  {i}")
    i += 2
```

>> Your output should look like this:

"
Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
"
>> The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
```
while True: 
    user_input = int(input('Enter a positive number: '))
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input <= 0:
            continue
        break

for i in range(0, user_input + 1):
    print(i)
```
>> Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.



## 3. Fizzbuzz

>> One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

>> Write a program that prints the numbers from 1 to 100.
for x in range(1,101):
    print(x)


>> For multiples of three print "Fizz" instead of the number

for x in range (1,101):
    if x % 3 == 0:
        print('Fizz')
    else:
        print(x)


>> For the multiples of five print "Buzz".

for x in range (1,101):
    if x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('buzz')
    else: 
        print(x)


>> For numbers which are multiples of both three and five print "FizzBuzz".

for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)

# note that order matters above. If 'fizzbuzz' was not first in order of ifs, the output would not answer the query

## 4. Display a table of powers.

>> Prompt the user to enter an integer.

x = int(input("Enter an integer: "))

>>  Display a table of squares and cubes from 1 to the value entered.
print()
print("number | squared | cubed")
print("-------| --------| ------")

for i in range(1, x + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3))

>> Ask if the user wants to continue.
>> Assume that the user will enter valid data.
>> Only continue if the user agrees to.
>> Example Output
"
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
"

>> Bonus: Research python's format string specifiers to align the table

## 5. Convert given number grades into letter grades.
while True: 
    numeric_grade = int(input("Enter a number grade: "))

    #convert grade to letter grade

    if numeric_grade >= 88:
        print('A')
    elif numeric_grade >= 80:
        print('B')
    elif numeric_grade >= 67:
        print('C')
    elif numeric_grade >= 60:
        print('D')
    else:
        print('F')

    # ask if user wants to continue 
       
    wants_to_continue = input('Do you want to continue? ')
    
    if wants_to_continue != 'yes':
        break

>> Prompt the user for a numerical grade from 0 to 100.
>> Display the corresponding letter grade.
>> Prompt the user to continue.
>> Assume that the user will enter valid integers for the grades.
>> The application should only continue if the user agrees to.
"Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0"

>> Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

## 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
books = [
    {"title": "The Splendid and the Vile", "author": "Erik Larson", "genre": "History"},
    {"title": "Waiting for Godot", "author": "Samuel Beckett" , "genre": "Theatre"},
    {"title": "The Birth of Tragedy" , "author": "Neitzsche" , "genre": "Philosophy"}]

for book in books:
    print("------")
    print("title: {}".format(book['title']))

>> Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

selected_genre = input("Please enter a genre: ")
selected_books = [book for book in books if book['genre'] == selected_genre]