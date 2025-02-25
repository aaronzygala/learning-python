"""

More function practice

"""

def get_sum_of_list(my_list):
    """
        This is a function that should take in a list of integers, 
        and return a sum of all the numbers in that list.

        To loop through a list, you can use a for loop or a while loop.
        Python conveniently allows you to loop through every item in the list, 
        without requiring a counter or an index.

        The syntax for this is:

            my_list = ["one", "two", "three", "four"]
        
            for x in my_list:
                print(x)

        This code prints out:
            "one"
            "two"
            "three"
            "four"

        So, if you see a for loop that looks like:
            for x in my_list
        You can imagine x being a variable that represents the current item 
        in a loop, as it loops through every item in the list.


        Using this concept, try to create a function that loops 
        through a list of numbers and adds them all together, 
        and then returns the total sum
    """
    pass

list_one = [0, 0, 1, 6]
list_two = [1, 8, 8, 8]
list_three = [1, 5, 9, 10]

if get_sum_of_list(list_one) == 7 and get_sum_of_list(list_two) == 25 and get_sum_of_list(list_three) == 25:
    print("Your function works!")
else:
    print("Your function does not work. Try again")

