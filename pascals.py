import math

n = 5 

def print_pascals_traingle():
    """
    Using the idea that each line of a pascal's traingle can be created by 
    raising 11 to some power; but breaks down after the 5th line
    Another observation is that the number of spaces in the begining and 
    in the end decrease as we go down the triangle
    """
    for line_no in range(0, n):
        pascal_number = math.pow(11, line_no)
        pascal_number = str(int(pascal_number))
        total_no_to_print = line_no + 1
        total_spaces_to_print = (n - line_no - 1)
        numbers_printed_counter = 1
        to_print = ''
        to_print += total_spaces_to_print * ' '
        for ff in pascal_number:
            to_print += ff
            if numbers_printed_counter < total_no_to_print:
                to_print += ' '
                numbers_printed_counter += 1
        to_print += total_spaces_to_print * ' '
        print(to_print)

print_pascals_traingle()
