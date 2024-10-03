"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    call_bubble_sort_for_restricted_coverage,
    cgi_decode,
    generate_fuzzer_values,
    perform_coverage_monitoring,
)


@pytest.mark.question_one_part_a
def test_coverage_monitoring_bubble_sort():
    """Confirm correctness of question part."""
    # check 1: run the question and track coverage
    # confirm that a total of seven lines are executed
    # and correctly tracked by the coverage monitor
    count_executed_lines = perform_coverage_monitoring(
        call_bubble_sort_for_restricted_coverage
    )
    assert count_executed_lines == 7


@pytest.mark.question_one_part_b
def test_generate_fuzzer_values():
    """Confirm correctness of question part."""
    max_length = 10
    result = generate_fuzzer_values(max_length)
    assert len(result) <= max_length, "Generated string is too long"
    char_start = 65
    char_range = 26
    result = generate_fuzzer_values(100, char_start, char_range)
    for char in result:
        assert (
            char_start <= ord(char) < char_start + char_range
        ), "Character is not in range"
    result = generate_fuzzer_values(0)
    assert result == "", "Empty string not generated"


@pytest.mark.question_one_part_c
def test_cgi_decode():
    """Confirm correctness of question part."""
    # check 1: Valid CGI-encoded string with a space
    assert cgi_decode("Hello%20World") == "Hello World", "Valid CGI-encoded string"
    # check 2: Valid CGI-encoded string with a colon
    assert (
        cgi_decode("Python%3A%20The%20best%20language") == "Python: The best language"
    ), "Valid CGI-encoded string"
    # check 3: Valid CGI-encoded string with a special character of < and >
    assert cgi_decode("%3Chtml%3E") == "<html>", "Valid HTML string"
    # check 4: Valid plus sign decodes to a blank space
    assert cgi_decode("+") == " ", "Valid plus sign decodes to a blank space"
    # check 5: Valid %20 decodes to a blank space
    assert cgi_decode("%20") == " ", "Valid %20 decodes to a blank space"
    # check 6: Valid %3A decodes to a colon
    assert cgi_decode("%3A") == ":", "Valid %3A decodes to a colon"
    # check 7: Valid %3C decodes to a less than sign
    assert cgi_decode("%3C") == "<", "Valid %3C decodes to a less than sign"
    # check 8: Valid %3E decodes to a greater than sign
    assert cgi_decode("%3E") == ">", "Valid %3E decodes to a greater than sign"
    # check 9: Invalid CGI-encoded string
    with pytest.raises(ValueError):
        cgi_decode("%GG")
    # check 10: Invalid CGI-encoded string
    with pytest.raises(ValueError):
        cgi_decode("%?a")
