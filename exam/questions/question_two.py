"""Question Two: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Dict, List, Union
from collections import Counter

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

# Part (a) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_minimum_value should:
# - Take a Dictionary where the keys are strings and the values are integers
# - Return an integer that represents the minimum value in the dictionary

# TODO: If the function is called with an invalid input (e.g., an empty
# dictionary), it should return None.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def find_minimum_value(dictionary: Dict[str, int]) -> Union[int, None]:
    """Return the minimum value in the provided dictionary."""
    return None


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_maximum_value should:
# - Take a list of lists of integers, called matrix, as its parameter
# - Return an integer that represents the maximum value in the matrix

# TODO: If the function is called with an invalid input (e.g., an empty
# matrix), it should return None.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def find_maximum_value(matrix):
    """Return the maximum value in the provided matrix."""
    return None


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function find_mode should:
# - Take a list of integers, called numbers, as its parameter
# - Return an integer that represents the mode of the list
# - If there are multiple modes, return the smallest one
# - If the list is empty, return None
# The mode of the list is the number that appears most frequently.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def find_mode(numbers: List[int]) -> Union[int, None]:
    """Determine the mode of a list of integers."""
    return 0


# }}}
