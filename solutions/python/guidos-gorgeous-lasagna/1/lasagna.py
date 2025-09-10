"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME= 40
PREPARATION_TIME=2

print(EXPECTED_BAKE_TIME)
        
  
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes

    :param number_of_layers: int - number of layers
    :return: int - number of layters with multipled by 2 

    Function that takes the no of layers the lasagna has been in the oven as
    an argument and returns the number of layters with updated value 
    """
    return number_of_layers * PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes

    :param number_of_layers: int - number of layers
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time 

    Function that takes number of layters and elapsed bake time as parameters and calculate the total     time time elapsed in minutes
    """
    return preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time
    


#  (you can copy and then alter the one from bake_time_remaining.)
