#******************************************************************************
# Author:           Kyle Noyes
# Lab:              Lab 1
# Date:             4/17/2022
#
# Description:      This program acts as a data validation tool and analysis
#                   tool. It's capable of managing basic arithmetic analysis
#                   with a number range calculator and checking if a user is
#                   inputting data correctly
#
# Input:            Program prompts user to select 1 of 6 tools for validation
#                   and basic arithmetic. 
#
# Output:           Will output reponses and answers to the tools used. In the
#                   case of the range analysis, it will handle all the maths to
#                   dispaly whether a number is within the range or not
#
# Sources:          Lab 1 specifications and videos. Also a downright unhealthy 
#                   amount of research/staring at stack overflow           
#******************************************************************************

# Import the valication functions
from input_validation import *


# define main, this will start the program. Set user_input as  false
# display all tools avaialble and their numberID
# set list start to 1 and list_end = length of list(tools)
# Welcome the user
# Begin While loop with false
# show user all tools available, prompt them to answer 1, 2, 3, 4, 5, or 6
# validate user input is an integer
# once validated, check if integer is within range list_start, list_end
# if validated, call that tool. Else, assume invalid and reprompt user for input
# if a user somehow manages to bypass the validation, call generic error as emergency
def main(user_input=False):
    tools = ["1 = input_int", "2 = input_float", "3 = input_string", "4 = y_or_no", \
"5 = select_item", "6 = range_analysis"]
    list_start = 1
    list_end = len(tools)
    print("Welcome! Here are all tools available for use:")
    while user_input is False:
        user_selection = input(F"{tools[0]}\n{tools[1]}\n{tools[2]}\n{tools[3]}\
\n{tools[4]}\n{tools[5]}\nPlease select one of the following programs by typing the program's number\
ID here: ")
        try:
            user_selection = int(user_selection)
        except:
            isInt_False()
            continue
        if isInt(user_selection) is True and isRange(list_start, len(tools), user_selection) is True:
            user_input = True
        elif isRange(list_start, len(tools), user_selection) is False:
            isRange_False(list_start, len(tools), user_selection)
            continue
        else:
            genericError()
            continue
    if user_selection == 1:
        input_int()
    elif user_selection == 2:
        input_float()
    elif user_selection == 3:
        input_string()
    elif user_selection == 4:
        y_or_n()
    elif user_selection == 5:
        select_item()
    elif user_selection == 6:
        range_analysis()
    else:
        genericError()


# define input_int, set valid = False
# prompt user to input a whole number
# validate that inpute is a whole number with validation call
# if it's not valud, reprompt the user for input and generate basic error
# if it's valid, print success message and set valid = true
def input_int(valid=False):
    while valid is False:
        user_input = input("Please enter a number to validate if it's whole or not: ")
        valid = isInt(user_input)
        if valid is True:
            print(F"{user_input} is a whole number.")
        else:
            print(F"{user_input} is not a whole number.")


# define input_float, set valid = False
# prompt user to input a number
# validate that input is a number with validation call
# if it's not valud, reprompt the user for input and generate basic error
# if it's valid, print success message and set valid = true
def input_float(valid=False):
    while valid is False:
        user_input = input("Please input data to validate if it's a number or not: ")
        valid = isFloat(user_input)
        if valid is True:
            print(F"{user_input} is a valid float number.")
        else:
            print(F"{user_input} is not a number.")


# define input_string, set valid = true
# call isString function to try and convert input to a flaot.
# if it fails, then we have a string and display success message
# else it's not a string and user need to retry
def input_string(valid=False):
    while valid is False:
        user_input = input("Please input data to validate if it's a string or not: ")
        valid = isString(user_input)
        if valid is True:
            print(F"{user_input} is a string.")
        else:
            print(F"{user_input} is not a string.")


# define y_or_no, set valid = flase
# prompt user to input answer to the quesiton
# if user inpout is a valid y/n and correct answer, display correct
# elif user input is a valid y/n and wrong answer, display incorrect
# else reprompt user for correct input and dusplay error
def y_or_n(valid=False):
    while valid is False:
        user_input = input("Does the German word \"gemütlich\" contain an umlaut? (yes/no): ")
        if isYesNo(user_input) is True and isYesNo_Value == "y":
            print("Correct!")
            valid = True
        elif isYesNo(user_input) is True and isYesNo_Value == "n":
            print("Wrong, \"ü\" is an umlaut")
            valid = True
        else:
            isYesNo_False()


# define select_items
# display functinality has been proven at program start
def select_item():
    print("Item selection has been proven with user_selection")


# define range_analysis, set value = false
# prompt user for lower bound number
# validate the response, continue it legal
# ask user if lower bound can equal the provided number to test
# validate the response, continue it legal
# pompt user for upper bound number
# validate the response, continue it legal
# ask user if upper bound cna equal the prodided number to test
# validate the response, continue it legal
# check if lower bound is equal to or greater than upper bound
# if so, this is an impossible range and function needs to be restarted
# let user know this is impossible and functionm is restarting
# ask user to input a number to check if it's within the range
# validate the response, continue it legal
# check if lower and upper bound equal and at least 1 can equal itself, it's legal
# if both can not, then it's another illegal entry and need to be restart
# if it's legal and allowed by the user (and validated), then proceed to the range analysis function
# if the bounds are not equal, then run the program as normal. Call range anylsis function
# return and display results
# prompt user if they would like try another range or not
# validate the response, continue it legal
# if yes, restart the function. If no, then close the program and go home for the day
def range_analysis(valid=False, value=False):
    while valid is False:
        user_lower = input("Please enter the lower bound of the range: ")
        if isFloat(user_lower) is False:
            isFloat_False()
            continue
        lower_inequality = input("Can the range number equal the lower bound? (yes/no): ")
        if isYesNo(lower_inequality) is False:
            isYesNo_False()
            continue
        elif isYesNo_Value(lower_inequality) == "y":
            lower_inequality = True
        else:
            lower_inequality = False
        user_upper = input("PLease enter the upper bound of the range: ")
        if isFloat(user_upper) is False:
            isFloat_False()
            continue
        if user_lower > user_upper:
            error = "Range is impossible"
            resolution = "please set the lower limit equal to or less than the upper limit"
            genericError(error, resolution)
        upper_inequality = input("Can the range number equal the upper bound? (yes/no): ")
        if isYesNo(upper_inequality) is False:
            isYesNo_False()
            continue
        elif isYesNo_Value(upper_inequality) == "y":
            upper_inequality = True
        else:
            upper_inequality = False
        user_number = input("Please enter a number to check if it's within the range or not: ")
        if isFloat(user_number) is False:
            isFloat_False()
            continue
        if user_lower == user_upper:
            if lower_inequality is True and upper_inequality is True:
                equal_allow = input("The range values are equal, do you want to proceed? (yes/no): ")
                if isYesNo(equal_allow) is True:
                    valid = isRange(user_lower, user_upper, user_number, lower_inequality, upper_inequality)
            else:
                error = "Range is impossible"
                resolution = "please allow the limits to equal the number or set limits != to eachouther"
                genericError(error, resolution)
                continue
        valid = isRange(user_lower, user_upper, user_number, lower_inequality, upper_inequality)
        if valid is False:
            user_input = print("Would you like to try another number range? (Yes/No): ")
            if isYesNo(user_input) is False:
                quit()
            else:
                continue
        else:
            user_input = input("Your number is in the range! Would you like to try another range? (Yes/No): ")
            if isYesNo_Value(user_input) == "n":
                quit()
            else:
                valid = False


# begin the program
main()
