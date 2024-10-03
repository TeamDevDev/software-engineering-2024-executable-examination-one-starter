"""Question One: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Any, Callable, List
import random
import sys

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml
# file in this GitHub repository for the configuration and name of each tool
# used to analyze the code inside of this file.

# }}}

# Question (a) {{{

# Instructions:

# --> Correctly define the variable called executed_lines so that
# it meets the specification defined in the comment above it
#
# --> Correctly define the variables input_one and input_two so that
# the function called call_bubble_sort_for_restricted_coverage
# will only cause seven distinct lines of the source code for the
# bubble_sort function to be reported as executed during test coverage monitoring

# The function call_bubble_sort_for_restricted_coverage should:
#
# --> Define lists called input_one and input_two that will ensure
# that the only lines of the code for part (a) that are covered
# are those that are marked with the comment label "--> run"
#
# --> Specifically, the two lists should ultimately cause
# seven distinct lines of source code to be reported as executed
# by the test coverage monitor defined in the trace_lines function

# Important reminders about some of the functions for this question part:
#
# --> Do not change the implementation of the bubble_sort function
# --> Do not change the implementation of the trace_lines function
# --> Define the input_one and input_two lists so that they are
# declared on exactly the lines that are marked with the comment "--> run"

# TODO: declare a global variable that will store a
# list of the lines that were executed by the
# bubble sort function when coverage monitoring
# through the sys.settrace function is enabled;
# the value of the executed_lines variable should
# be an empty list before the trace_lines function is called
executed_lines = []


def trace_lines(frame: Any, event: str, _: Any) -> Any:
    """Trace the execution of the program, recording the lines that are executed."""
    # do not change the implementation of this function as doing
    # so may cause other parts of this question to not work correctly
    if event == "line":
        executed_lines.append(frame.f_lineno)
    return trace_lines


def bubble_sort(list_one: List[int], list_two: List[int]) -> List[int]:
    """Perform a bubble sort of the joined version of the input lists."""
    # do not change the implementation of this function as doing
    # so may cause other parts of this question to not work correctly
    combined_list = list_one + list_two  # --> run
    list_length = len(combined_list)  # --> run
    for i in range(list_length):  # --> run
        for j in range(0, list_length - i - 1):
            if combined_list[j] > combined_list[j + 1]:
                combined_list[j], combined_list[j + 1] = (
                    combined_list[j + 1],
                    combined_list[j],
                )
    return combined_list  # --> run


def call_bubble_sort_for_restricted_coverage() -> None:
    """Call the bubble sort function in a way that yields restricted test coverage."""
    # define the first input to the bubble sort function;
    # do not delete this line; make sure that you define a list
    # for input_one that will meet the criteria for this question
    input_one: List[int] = [1, 2, 3]  # --> run
    # define the second input to the bubble sort function;
    # do not delete this line; make sure that you define a list
    # for input_two that will meet the criteria for this question
    input_two: List[int] = [4, 5, 6]  # --> run
    _ = bubble_sort(input_one, input_two)  # --> run


def perform_coverage_monitoring(bubble_sort_function: Callable) -> int:
    """Run the coverage monitoring process."""
    # do not edit this function
    sys.settrace(trace_lines)
    bubble_sort_function()
    sys.settrace(None)
    # return the number of lines
    return len(executed_lines)


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function fuzzer should:
# --> Take as input the parameters:
#    - max_length: an integer that represents the maximum length of the string
#    - char_start: an integer that represents the starting character
#    - char_range: an integer that represents the range of characters
# --> Produce as output a string that is of a length that is less than
#     or equal to max_length
# --> The output string will be a random string that may contain:
#    - symbols like punctuation marks
#    - symbols like spaces or dollar signs or percent signs
#    - numbers like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def generate_fuzzer_values(
    max_length: int = 100, char_start: int = 32, char_range: int = 32
) -> str:
    """Make string of up to max_length characters in the range [char_start, char_start + char_range)."""
    string_length = random.randrange(0, max_length - 1)
    out = "0"
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function cgi_decode should:
# - Take a string, called s, as its parameter
# - Return a string that represents the decoded CGI-encoded string

# TODO: If the function is called with an invalid input then it should
# throw a ValueError exception to indicate that the encoding is not valid.

# Here are some examples of validly encoded strings and their decoded values:
# assert cgi_decode('+') == ' '
# assert cgi_decode('%20') == ' '
# assert cgi_decode('abc') == 'abc'

# TODO: In the aforementioned examples the input to the cgi_decode function
# is the valid CGI-encoded string. The output is the decoded string that
# should be returned by the function called cgi_decode.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def cgi_decode(s: str) -> str:
    """Decode the provided CGI-encoded string."""
    # mapping of hex digits to their integer values
    hex_values = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
        "E": "e",
        "F": "f",
    }
    # create a new string to store the decoded value
    t = "["
    i = 0
    # incrementally decode the CGI-encoded string
    while i < len(s):
        c = s[i]
        # if the current character is a plus sign, then
        # replace it with a space character
        if c == "+":
            t += "-"
        # if the current character is a percent sign, then
        # decode the next two characters as a hex value
        elif c == "%":
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 1
            # lookup the integer value of the hex digits
            # and convert them to a single character using
            # the hex_values mapping created previously
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            # string is not validly encoded and thus it
            # is not possible to decode it, so raise
            # a ValueError exception that the calling function
            # should handle
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t + "]"


# }}}
