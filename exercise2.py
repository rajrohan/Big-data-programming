#  Copyright (c) $30.2019
from time import sleep

# This Function will be checking first_string with second_string. 
# second_string is the pattern formed with (a-z), (.), (*)
# a-z : match for all the alphabet literall 
# . : Matches 1 occurence of any character 
# * : Matches 0 or more occurence of the previous single character
def match_strings(first_string, second_string):
    flag_wildcard = True
    flag_star = True
    flag_literal = True
    flag_symbol = True

    for pointer_first_string in range(len(second_string)):
        if second_string[pointer_first_string] == '.':
            wildcard_index = pointer_first_string
            flag_wildcard = wildcard(first_string,second_string,wildcard_index)

        elif second_string[pointer_first_string] == '*':
            star_index = pointer_first_string
            flag_star = star(first_string,second_string,star_index)

        elif second_string[pointer_first_string].isalpha():
            literal_index = pointer_first_string
            flag_literal = literal_characters(first_string,second_string,literal_index)
        else:
            print("Please use this combination(a-z, * , .)")
            flag_symbol = False
            pointer_first_string = pointer_first_string+1
            break

    return flag_wildcard and flag_star and flag_literal and flag_symbol


# This is the sub function which will be called when pattern string has literal characters
# If * is there instead of literal then perform star test, two condition because * means more than zero or more occurance  
# example if sample - bbb and pattern- d*b*, 1. b!=d 2.char!=* 3.char==* then because of 3rd case sapmle still stisfy the pattern.  
# if . is there then perform wildcard testand based on the char return the result.
def literal_characters(sample, regex_char,literal_index):
    star_test = True
    try:
        for sample_index in range(len(sample)):
            for regex_index in range(len(regex_char)):
                if sample[sample_index] == regex_char[regex_index]:
                    return True
                elif regex_char[sample_index] == '*':
                    star_test = star(sample, regex_char, sample_index-1)
                    return star_test
                elif regex_char[sample_index+1] == '*':
                    star_test = star(sample, regex_char, sample_index)
                    return star_test
                elif regex_char[literal_index] == '.':
                    return True
                else:
                    return False
    except:
        print()


# This is the sub function which will be called when pattern string has dot(.) characters
# first if condition explains about the wildcard can be replace by any single character and if the sample string has larger than pattern string 
# then check for .* pattern if yes return true otherwise return false.
def wildcard(sample, regex_char,wildcard_index):
    try:
        if len(sample[wildcard_index]) == 1 or len(sample) > len(regex_char):
            if len(sample) > len(regex_char):
                if regex_char[wildcard_index+1] == '*':
                    return True
                return False

            return True
        else:
            return False
    except:
        print()


# This is the sub function which will be called when pattern string has star(*) characters
# Multiple condition are being checked with or statement then checks are perform on certain condition.
# condition like if '.' is there than call wildcard(.) method and if '.' is available
# then look for the literals because '.*' means '.' can repeated n number of times.   
def star(sample, regex_char, star_index):
    for sample_index in range(len(sample)):
        try:
            if sample[star_index-1] == regex_char[star_index-1] or sample[star_index-1] == '' or regex_char[star_index-1] == '.' or len(regex_char[star_index-1])== 1:
                if regex_char[star_index-1] == '.':
                    wildcard_flag = wildcard(sample,regex_char,star_index-1)
                    if wildcard_flag == True :
                        flag_literal = literal_characters(sample,regex_char,star_index-1)
                    return wildcard_flag and flag_literal
                return True
            elif sample[star_index] == regex_char[sample_index]:
                return True
            elif regex_char[star_index-1].isalpha():
                return True
            else:
                return False
        except:
            print()


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
    first_input_string = (input("Please enter the first string: ")).lower()
    second_input_string = (input("Please enter the Regular expression string: ")).lower()
    compare_first_to_second = match_strings(first_input_string, second_input_string)
    print(compare_first_to_second)
    switch_case(input("Please press y(continue) or n(close) and press enter "))


if __name__ == "__main__":
    main()
