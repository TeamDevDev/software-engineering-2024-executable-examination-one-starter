"""Confirm the correctness of functions in question_three."""

from typing import List

import pytest

# ruff: noqa: PLR2004
from questions import question_three
from questions.question_three import (
    classify_triangle,
    compute_coverage_difference,
    compute_coverage_intersection,
    count_nested_lists,
    create_empty_lists,
)


@pytest.mark.question_three_part_a
def test_create_empty_lists():
    """Confirm correctness of question part."""
    # test when count is 0
    result = create_empty_lists(0)
    assert isinstance(result, List), "Result should be a list"
    assert len(result) == 0, "List should be empty when count is 0"
    # test when count is 1
    result = create_empty_lists(1)
    assert isinstance(result, List), "Result should be a list"
    assert len(result) == 1, "List should have one empty list when count is 1"
    assert (
        result[0] == []
    ), "The only list in the output should be empty when count is 1"
    # test when count is 3
    result = create_empty_lists(3)
    assert isinstance(result, List), "Result should be a list"
    assert len(result) == 3, "Result list should have three empty lists when count is 3"
    for i in range(3):
        assert result[i] == [], f"The list at index {i} should be empty when count is 3"


@pytest.mark.question_three_part_a
def test_count_nested_lists():
    """Confirm correctness of question part."""
    # test when nested_list is empty
    result = count_nested_lists([])
    assert result == 0, "Result should be 0 when the nested list is empty"
    # test when nested_list contains one empty list
    result = count_nested_lists([[]])
    assert (
        result == 1
    ), "Result should be 1 when the nested list contains one empty list"
    # test when nested_list contains three empty lists
    result = count_nested_lists([[], [], []])
    assert (
        result == 3
    ), "Result should be 3 when the nested list contains three empty lists"
    # test when nested_list contains non-list items
    result = count_nested_lists([1, "a", [], 2.2])  # type: ignore
    assert (
        result == 1
    ), "Result should be 1 when the nested list contains one list and other non-list items"
    # test when nested_list contains non-list items
    result = count_nested_lists([1, "a", [], 2.2, [2]])  # type: ignore
    assert (
        result == 2
    ), "Result should be 2 when the nested list contains two lists and other non-list items"
    # test when nested_list contains nested lists
    result = count_nested_lists([[1, 2, 3], [56, 4, 9, 0], [2, 3, 4]])  # type: ignore
    assert (
        result == 3
    ), "Result should be 3 when the nested list contains three nested lists"


@pytest.mark.question_three_part_b
def test_classify_triangle():
    """Confirm correctness of question part."""
    assert (
        classify_triangle(3, 3, 3) == question_three.triangle.Equilateral
    ), "Failed on case with all sides equal"
    assert (
        classify_triangle(3, 4, 3) == question_three.triangle.Isosceles
    ), "Failed on case with two sides equal"
    assert (
        classify_triangle(3, 4, 5) == question_three.triangle.Scalene
    ), "Failed on case with no sides equal and ascending values"
    assert (
        classify_triangle(5, 4, 3) == question_three.triangle.Scalene
    ), "Failed on case with no sides equal and descending values"
    assert (
        classify_triangle(3, 3, 4) == question_three.triangle.Isosceles
    ), "Failed on case with first and second sides equal"
    assert (
        classify_triangle(3, 4, 4) == question_three.triangle.Isosceles
    ), "Failed on case with second and third sides equal"


@pytest.mark.question_three_part_c
def test_compute_coverage_intersection():
    """Confirm correctness of question part."""
    assert compute_coverage_intersection([1, 2, 3], [1, 2, 3]) == [
        1,
        2,
        3,
    ], "Failed on case with identical coverage reports"
    assert (
        compute_coverage_intersection([1, 2, 3], [4, 5, 6]) == []
    ), "Failed on case with no common coverage"
    assert compute_coverage_intersection([1, 2, 3], [2, 3, 4]) == [
        2,
        3,
    ], "Failed on case with partial overlap"
    assert compute_coverage_intersection([1, 2, 3], [3, 2, 1]) == [
        1,
        2,
        3,
    ], "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_intersection([], []) == []
    ), "Failed on case with empty coverage reports"


@pytest.mark.question_three_part_c
def test_compute_coverage_difference():
    """Confirm correctness of question part."""
    assert (
        compute_coverage_difference([1, 2, 3], [1, 2, 3]) == []
    ), "Failed on case with identical coverage reports"
    assert compute_coverage_difference([1, 2, 3], [4, 5, 6]) == [
        1,
        2,
        3,
    ], "Failed on case with no common coverage"
    assert compute_coverage_difference([1, 2, 3], [2, 3, 4]) == [
        1
    ], "Failed on case with partial overlap"
    assert (
        compute_coverage_difference([1, 2, 3], [3, 2, 1]) == []
    ), "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_difference([], []) == []
    ), "Failed on case with empty coverage reports"
