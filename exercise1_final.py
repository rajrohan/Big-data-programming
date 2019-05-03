#  Copyright (c) $Rohan

from time import sleep


# Functions Return the list of all matching string of any length
# Function is used for checking lcs(Longest common sub-sequences) for each literals
# Example first_string- ABCD second_string-XYZABC, checking lcs start with A then for B and so on.
def check_each_char(first_string, second_string,):
    result = []
    length__first_string = len(first_string)
    for i in range(length__first_string):
        result.append(find_lcs(first_string, second_string, i))
    return result


# This function returns the longest common string
# This is core logic for finding the Longest common sub-sequences
# This will check for each matching string in second string, If not matches then move the second string pointer only
# when match happen then store the literal and move the pointer.
def find_lcs(first_string, second_string, index_position_first_string):
    result = ''
    length__first_string = len(first_string)
    length__second_string = len(second_string)
    index_position_second_string = 0
    for pointer_first_string in range(index_position_first_string, length__first_string):
        for pointer_second_string in range(index_position_second_string, length__second_string):
            if first_string[pointer_first_string] != second_string[pointer_second_string]:
                pointer_second_string = pointer_second_string + 1
            else:
                result = result + first_string[pointer_first_string]
                pointer_first_string = pointer_first_string + 1
                index_position_first_string = pointer_first_string
                pointer_second_string = pointer_second_string + 1
                index_position_second_string = pointer_second_string
                break
    return result


# This function is to check whether the data is empty or not.
# Also check and return the unique value in the sample list
# Example ['a','b','c','a'] the it'll return ['a','b','c']
def unique(data):
    if len(data) == 0:
        print("There is no common sub-sequence")
    else:
        return list(dict.fromkeys(data))


# This function is used to return the maximum length of string
def check_lcs(lcs1, lcs2):
    # lcs1 = lcs1.upper()
    # lcs2 = lcs2.upper()
    multiple_lcs = lcs1 + lcs2
    le = max(len(string) for string in multiple_lcs)
    print("Longest common sub-sequences: ", [string for string in multiple_lcs if len(string) == le])


# Basic Switch to test the application without rerun the source code.
def switch_case(continue_exit):
    continue_exit = continue_exit.upper()
    if continue_exit == 'Y':
        main()
    elif continue_exit == 'N':
        print("Exiting the application...")
        sleep(1)
    else:
        print("Please enter either y or n")

# Main function
def main():
    first_input_string = input("Please enter the first string: ")
    second_input_string = input("Please enter the second string: ")
    lcs1_2 = check_each_char(first_input_string, second_input_string)
    lcs2_1 = check_each_char(second_input_string, first_input_string)
    print("All the common strings ", unique(lcs1_2+lcs2_1))
    check_lcs(lcs1_2, lcs2_1)
    switch_case(input("Please press y(continue) or n(close) and press enter "))

# Application startpoint.
if __name__ == "__main__":
    main()