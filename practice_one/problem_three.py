"""

Final problem (HARD MODE)

Write a function called "is_leap_year(year)" that determines if a given year is a leap year.

Here are the requirements for a leap year:

    A leap year (in the Gregorian calendar) occurs:

        In every year that is evenly divisible by 4.

        Unless the year is evenly divisible by 100, 
        in which case it's only a leap year if the year is also evenly divisible by 400.

Your function should return True if it is a leap year, and false if not

"""

if (not is_leap_year(1997)) and (not is_leap_year(1900)) and (is_leap_year(2000)):
    print("Your function works!")
else:
    print("Your function does not work. Try again.")