
#   A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#   Create a dict suitable for decoding month names to numbers.
#   use string operations to split the date into 3 items using the '-' character.
#   Translate the month and return a tuple.
#   In the end we have a date 'dd-MMM-yy' format and we get a new string 'd-m-y'

months = {'JAN' : '1', 'FEB' : '2', 'MAR' : '3', 'APR' : '4', 'MAY' : '5', 'JUN' : '6', 'JUL' : '7', 'AUG' : '8', 'SEP' : '9', 'OCT' : '10', 'NOV' : '11', 'DEC' : '12'}

user_input = input("Enter a date in the format 'dd-MMM-yy' ex. '8-MAR-85': ")           # Takes user input and then saves it to our variable.
try:
    print('-'.join([months.get(i, i) for i in user_input.split('-')]))
except ValueError:
    print("Error: must be in 'dd-MMM-yy' format. ")