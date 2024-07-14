# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?

class Time:
    def min_to_sec(min):
        seconds = min * 60
        print(seconds)

    min_to_sec(5)

    def hour_to_sec(hours):
        seconds = hours * 3600
        print(seconds)

    hour_to_sec(24)

    def days_to_hours(days):
        hours = days * 24
        print(hours)

    days_to_hours(30)

    def hours_to_min(hours):
        min = hours * 60
        print(min)

    hours_to_min(744)



    # 86,400 seconds in a day
    # 720 hours in a month
    # 44,640 min in August

 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def return_middle_letter(string):
    length = len(string)
    if length % 2 == 0:
        print('String has even number of letters.')
    else:
        middle_index = length // 2
        print(string[middle_index])

return_middle_letter('sebastian')

return_middle_letter('sebastiann')

# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

def hide_card_number(cardnum):
    length = len(cardnum)
    hidden_nums = '*' * (length - 4)
    show_nums = cardnum[-4:]

    print(hidden_nums + show_nums)

hide_card_number('1234567894444')
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->

def online_count(statuses):
    online = 0
    for status in statuses.values():
        if status == "online":
            online += 1
    return online

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

num_online = online_count(statuses)
print(f"Number of people online: {num_online}")
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

def give_discount(price, discount):
    amt_off = price * (discount * 0.01)
    new_price = price - amt_off
    print(new_price)

give_discount(100, 20)

# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->

def pythagorean(adjacent, opposite):
    a_square = adjacent * adjacent
    b_square = opposite * opposite
    c_square = a_square + b_square
    hypotenuse = c_square ** 0.5
    print(hypotenuse)

pythagorean(4, 4)

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->

def fibonacci(num1, num2):
    numbers = [num1, num2]
    while len(numbers) < 9:
        next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)

    print(numbers)

fibonacci(1, 1)

# ---------------------------------
