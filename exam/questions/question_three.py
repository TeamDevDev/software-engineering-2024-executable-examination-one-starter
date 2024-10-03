"""Question Three: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List
from dataclasses import dataclass

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

# Implement the following function that creates a containing list of empty
# lists (i.e., a list that contains lists that do not have any contents)

# Function description:
# The function create_empty_lists should:
# --> Return a list that contains a total of count empty lists
# --> For instance,
#     -- create_empty_lists(1) will create the output [[]] because
#     the function was instructed to create a list that contains 1 empty list
#     -- create_empty_lists(2) will create the output [[], []] because
#     the function was instructed to create 2 empty lists in the containing list

# Implement the following function that counts the number of lists
# that are inside of a containing list

# Function description:
# The function count_nested_lists should:
# --> Return the number of lists that are inside of a containing list
# --> For instance, when the function is provided with the input [[]]
#     the function should return 1 because there is one list in the containing list
# --> For instance, when the function is provided with the input [[], []]
#     the function should return 2 because there are two lists in the containing list
# --> Whenever the function is provided with an empty list, the function should return 0
# --> Whenever the function is provided with a list that contains non-list items,
#     the function should only count the lists and ignore the non-list items


def create_empty_lists(count):
    """Create a list containing count empty lists."""
    empty_list_container = []
    return empty_list_container


def count_nested_lists(nested_list):
    """Count the number of nested lists in a list."""
    # initialize the count to zero
    count = 0
    # return the count of the nested lists
    return count


# }}}

# Part (b) {{{

# Instructions:
# Fix the defect(s) inside of the classify_triangle function so that it
# produces the correct output for each of the three major cases for a triangle
# and passes the test suite defined in the function in these functions:
# ---> test_classify_triangle_weak_oracle
# ---> test_classify_triangle_strong_oracle

# Function description:
# The function classify_triangle should:
# --> Return "Equilateral" when the function receives three equal sides
# --> Return "Isosceles" when the function receives two equal sides
# --> Return "Scalene" when the function receives three unequal sides

# When the function called classify_triangle is provided with the following inputs
# it will produce the stated outputs given after the word "return":
# --> 1, 1, 1 the function should return "Equilateral"
# --> 1, 1, 2 the function should return "Isosceles"
# --> 1, 2, 3 the function should return "Scalene"

# The following web sites contain a visual representation of the triangle types:
# Equilateral: https://en.wikipedia.org/wiki/Equilateral_triangle
# Isosceles: https://en.wikipedia.org/wiki/Isosceles_triangle
# Scalene: https://en.wikipedia.org/wiki/Scalene_triangle

# Please note that it is acceptable for you to view the Wikipedia definitions
# of these triangles when you are working on the answer to this function. With
# that said, if you reference other web sites beyond those three that are
# referenced in the above comments, then you must cite those as sources inside
# of the README.md file. Please remember that the failure to cite your sources
# is considered a violation on the Allegheny College Honor Code.


@dataclass(frozen=True)
class Triangle:
    """Define the Triangle dataclass for constant(s)."""

    Equilateral: str
    Isosceles: str
    Scalene: str


# create an instance of the Triangle dataclass;
# this is used to store the triangle types and
# to attach more meaning to the string constants
triangle = Triangle(Equilateral="Equilateral", Isosceles="Isosceles", Scalene="Scalene")


def classify_triangle(a: int, b: int, c: int) -> str:
    """Determine whether or not a triangle is equilateral, isosceles, or scalene."""
    if a == b:
        if b == c:
            return triangle.Isosceles
        else:
            return triangle.Scalene
    elif b == c:
        return triangle.Equilateral
    elif a == c:
        return triangle.Isosceles
    else:
        return triangle.Scalene


# }}}


# Part (c) {{{

# Instructions:
# Implement both of the following functions so that they
# adhere to their function descriptions and pass the test suite

# Function description:
# The compute_coverage_intersection function should:
# --> Accept as input two coverage reports where each report is
#     a list of integers that represent the covered lines in a function
# --> Return a list of integers that represents the coverage intersection
#     between the two coverage reports
# --> The intersection of two coverage reports is the set of lines that
#     are covered by the tests as evidenced by appearing in both coverage reports
# --> Intuitively, the coverage intersection is the set of lines that are
#     evident in both of the coverage reports

# Function description:
# The compute_coverage_difference function should:
# --> Accept as input two coverage reports where each report is
#     a list of integers that represent the covered lines in a function
# --> Return a list of integers that represents the coverage difference
#     between the two coverage reports
# --> The difference of two coverage reports is the set of lines that
#     are covered by the tests in the first report but not covered
#     by the tests in the second report
# --> Intuitively, the coverage difference is the set of lines that are
#     evident in the first coverage report but not in the second one

# TODO: If you are not familiar with the concept of a set intersection
# and/or a set difference, please refer to the test cases in the
# file called tests/test_question_three.py in this GitHub repository.


def compute_coverage_intersection(
    coverage_report_one: List[int], coverage_report_two: List[int]
) -> List[int]:
    # initialize the coverage intersection to be an empty list
    coverage_intersection = []
    # return the coverage intersection
    return coverage_intersection


def compute_coverage_difference(coverage_report_one, coverage_report_two):
    # initialize the coverage difference to be an empty list
    coverage_difference = []
    return coverage_difference


# }}}
