"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import find_maximum_value, find_minimum_value, find_mode


@pytest.mark.question_two_part_a
def test_find_minimum_value():
    """Confirm correctness of question part."""
    # check 1: Dictionary with positive values
    dictionary = {"a": 5, "b": 7, "c": 3}
    minimum_positive = find_minimum_value(dictionary)
    assert (
        3 == minimum_positive and minimum_positive is not None
    ), "Minimum positive value in dictionary"
    # check 2: Dictionary with negative values
    dictionary = {"a": -2, "b": 5, "c": 1}
    minimum_negative = find_minimum_value(dictionary)
    assert (
        -2 == minimum_negative and minimum_negative is not None
    ), "Minimum negative value in dictionary"
    # check 3: Dictionary with a single element
    dictionary = {"a": 10}
    minimum_single = find_minimum_value(dictionary)
    assert (
        10 == minimum_single and minimum_single is not None
    ), "Minimum value in single-element dictionary"
    # check 4: Empty dictionary
    dictionary = {}
    minimum_empty = find_minimum_value(dictionary)
    assert minimum_empty is None, "Minimum value in empty dictionary"


@pytest.mark.question_two_part_b
def test_find_maximum_value():
    """Confirm correctness of question part."""
    # check 1: Matrix with positive values
    matrix = [[5, 7, 3], [1, 9, 2], [6, 4, 8]]
    maximum_positive = find_maximum_value(matrix)
    assert 9 == maximum_positive, "Maximum positive value in matrix"
    # check 2: Matrix with negative values
    matrix = [[-2, 5, 1], [-3, 0, 6], [-1, -4, 7]]
    maximum_negative = find_maximum_value(matrix)
    assert 7 == maximum_negative, "Maximum negative value in matrix"
    # check 3: Matrix with a single element
    matrix = [[10]]
    maximum_single = find_maximum_value(matrix)
    assert 10 == maximum_single, "Maximum value in single matrix"
    # check 4: Empty matrix
    matrix = []
    maximum_empty = find_maximum_value(matrix)
    assert maximum_empty is None, "Maximum value in empty matrix"


@pytest.mark.question_two_part_c
def test_find_mode():
    """Confirm correctness of question part."""
    # test when the list is empty
    assert find_mode([]) is None, "Mode of an empty list should be None"
    # test when the list has one number
    single_number = [5]
    assert (
        find_mode(single_number) == 5
    ), "Mode of a list with one number should be that number"
    # test when all numbers in the list are the same
    same_numbers = [2, 2, 2, 2]
    assert (
        find_mode(same_numbers) == 2
    ), "Mode of a list with the same numbers should be that number"
    # test when the list has one mode
    one_mode = [1, 2, 2, 3]
    assert (
        find_mode(one_mode) == 2
    ), "Mode of a list with one mode should be that number"
    # test when the list has multiple modes
    multiple_modes = [1, 2, 2, 3, 3]
    assert (
        find_mode(multiple_modes) == 2
    ), "Mode of a list with multiple modes should be the smallest mode"
    # test a longer example from StackOverflow for a minimal mode
    # Reference:
    # https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
    multiple_modes_longer = [1, 1, 1, 1, 2, 3, 3, 3, 3, 4]
    assert (
        find_mode(multiple_modes_longer) == 1
    ), "Mode of a longer list with multiple modes should be the smallest mode"
