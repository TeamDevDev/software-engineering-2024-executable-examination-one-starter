"""Pytest configuration for the executable examination."""


def pytest_configure(config):
    """Add markers to the pytest configuration."""
    # Question 1
    config.addinivalue_line("markers", "question_one_part_a: Question 1 Part (a)")
    config.addinivalue_line("markers", "question_one_part_b: Question 1 Part (b)")
    config.addinivalue_line("markers", "question_one_part_c: Question 1 Part (c)")
    # Question 2
    config.addinivalue_line("markers", "question_two_part_a: Question 2 Part (a)")
    config.addinivalue_line("markers", "question_two_part_b: Question 2 Part (b)")
    config.addinivalue_line("markers", "question_two_part_c: Question 2 Part (c)")
    # Question 3
    config.addinivalue_line("markers", "question_three_part_a: Question 3 Part (a)")
    config.addinivalue_line("markers", "question_three_part_b: Question 3 Part (b)")
    config.addinivalue_line("markers", "question_three_part_c: Question 3 Part (c)")
