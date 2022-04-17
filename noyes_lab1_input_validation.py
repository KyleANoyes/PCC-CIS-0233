# define genericError, default with false values
#   if a value = false, no data was entered, do not compute
#   else print invalid data message with error and resolution
def genericError(error=False, resolution=False):
    if error is False:
        print("Unknown error, please contact your administrator")
    else:
        print(F"Invalid data or input. {error}, {resolution}")


# define wholeNum, default false num value
#   if num is false, no data was provided
#       call generic error function, provid error and resolution
#   elif call function isInt with num argument
#       if function return = true, return true
#   else input is not a whole num, call generic error function
def wholeNum(num=False):
    if num is False:
        error = "No data was entered"
        resolution = "please enter a whole number"
        genericError(error, resolution)
    elif isInt(num) is True:
        return True
    else:
        return False


# define isInt, internall function not accessible by user, take num argument
#   try to convert argument to int
#   if successfull, return true
#   else return false
def isInt(num):
    try:
        num = int(num)
        return True
    except:
        return False

# define isInt_False, internall function to call error generator
#   create error, create resolution
#   call genericError generator
def isInt_False():
    error = "Input is not a whole number"
    resolution = "please only enter a whole number"
    genericError(error, resolution)


# define isFloat, internall function not accessible by user, take num argument
#   try to convert argument to float
#   if successfull, return true
#   else return false
def isFloat(num=False):
    if num is False:
        error = "No data was entered"
        resolution = "please enter a number"
        genericError(error, resolution)
    try:
        num = float(num)
        return True
    except:
        return False


# define isFloat_False, internall function to call error generator
#   create error, create resolution
#   call genericError generator
def isFloat_False():
    error = "Input is not a number"
    resolution = "please only enter a number"
    genericError(error, resolution)


# define isYesNo, internal function not accessible by user, take boo argument
#   check if boo is not a float (this will also catch integers)
#       if not, convert input to string (for data confirmation / scrubbing)
#       convert boo to lowercase
#       get first letter in boo
#       if first letter is y or n, return True (calling program should handle the input)
#       else return False
def isYesNo(boo):
    if isFloat(boo) is False:
        boo = strConvert(boo)
        boo.lower()
        if boo[0] == "y":
            return True
        elif boo[0] == "n":
            return True
    else:
        return False


# define isYesN0_Value
#   Follow same structure as function above, but returns a y/n string
#   This is used in some instanced to capture whether a user want to continue or not
#   and either value can be a true statment within the isYesNo function
def isYesNo_Value(boo):
    if isFloat(boo) is False:
        boo = strConvert(boo)
        boo.lower()
        if boo[0] == "y":
            return "y"
        elif boo[0] == "n":
            return "n"


# define isYesNo_False
#   call error generator to let user know their y/n was not inputted correctly
def isYesNo_False():
    error = "Input was not \"Yes\" or \"No\""
    resolution = "please only enter \"Yes\" or \"No\""
    genericError(error, resolution)


# define isString function with text argument
#   check if text is not a float (this will also catch integers)
#   if not, input is a string. Return True
#   else, input is not a string. Return False
def isString(text):
    if isFloat(text) is False:
        return True
    else:
        return False


# define strConvert, take argument i (yea I'm being lazy, but come on, there are only 2 lines lol),
# also this is another internal function that's non user accessible. If I am calling this function,
# then I am doing so in a very deliberate manner and need to know my variable is 100% a string.
# I read function calls like this in a much more serious manner vs. a generic str(<variable>).
#   return i as string
def strConvert(i):
    return str(i)


# Python spaghetti inbound
# define isRange, this is an internal function that the user does not interact with
#   Check if there is data that's been included with the function call. Call error if no data
#   Check if lower or upper bound is equal to user supplied number
#       if it is, check if equality is allowed (it is by default)
#           if equality is allowed, then return True. Return false if not allowed
#   check if the user supplied number (assuming equality not allowed) is within range
#       if so, return True. Return false if not true
#   if all else fails, call the error function for a generic error message and termination
def isRange(lower=False, upper=False, number=0, lower_inequality=True, upper_inequality=True):
    if lower is False and upper is False:
        isRange_False()
        return False
    elif lower is False or upper is False:
        isRange_False(lower, upper)
        return False
    elif number == lower:
        if lower_inequality is True:
            return True
        else:
            return False
    elif number == upper:
        if upper_inequality is True:
            return True
        else:
            return False
    elif number > lower and number < upper:
        return True
    elif number < lower or number > upper:
        return False
    else:
        isRange_False(lower, upper)


# define isRange_False generic error messages
#   check if lower or upper are false, if true for either, call error generator
#       These should be impossible to ever hit, but I have them here as a fail-safe
#   check if lower bound is > upper bound. Should be impossible, but another fail-safe
#   if number is not within the range, call error generator with that message
def isRange_False(lower=False, upper=False, number=False):
    if lower is False:
        error = "Lower bound is not defined"
        resolution = "please define the lower limit"
        genericError(error, resolution)
    elif upper is False:
        error = "Upper bound is not defined"
        resolution = "please define the upper limit"
        genericError(error, resolution)
    elif lower is False and upper is False:
        error = "No valid range values have been defined"
        resolution = "please define valid range values"
        genericError(error, resolution)
    elif lower > upper:
        error = "Lower bound is greater than upper bound"
        resolution = "please set the lower bound to be less than the upper bound"
        genericError(error, resolution)
    elif number < lower or number > upper:
        error = "Number is not within the range"
        resolution = "please select a number within the range / options"
        genericError(error, resolution)
    else:
        genericError()
