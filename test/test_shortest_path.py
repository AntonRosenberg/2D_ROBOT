import pytest
import numpy as np
from main import main
import sys
import os

# Test cases and their expected outputs
test_cases_shortest_distance = [
    {
        "input": "test/data/NoObstacles.yaml",
        "expected_path": [(2, 2), (98, 98)]  
    },
    {
        "input": "test/data/ObstacleOutsideBounds.yaml",
        "expected_path": [(2, 2), (10.0, 5.0), (20.0, 15.0), (60.0, 80.0), (80.0, 90.0), (98, 98)]  
    },
    {
        "input": "test/data/TwoObstacles.yaml",
        "expected_path": [(2, 2), (8.0, 12.0), (60.0, 80.0), (80.0, 90.0), (98, 98)]  
    },
    {
        "input": "test/data/OverlappingObstacles.yaml",
        "expected_path": [(2, 2), (25.0, 50.0), (35.0, 60.0), (98, 98)]  
    },
]

@pytest.mark.parametrize("test_case", test_cases_shortest_distance)
def test_shortest_distance(monkeypatch, test_case):
    # Mock command line arguments
    output_file = "test_output.txt"
    monkeypatch.setattr(sys, 'argv', ['main.py', test_case['input'], output_file])
    
    # Run the program
    main()

    path_output = []
    # Read the resulting output file
    with open(output_file, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            path_output.append((int(numbers[0]), int(numbers[1])))

    # Check if the path is correct
    assert len(path_output) == len(test_case['expected_path']), "Path length mismatch"
    for expected, actual in zip(test_case['expected_path'], path_output):
        assert expected == actual, f"Expected {expected}, but got {actual}"

    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)


# Test cases and their expected outputs
test_cases_shortest_time = [
    {
        "input": "test/data/NoObstacles.yaml",
        "expected_path": [(2, 2), (98, 98)]  
    },
    {
        "input": "test/data/ObstacleOutsideBounds.yaml",
        "expected_path": [(2, 2), (10, 5), (20, 15), (60, 80), (80, 90), (98, 98)]  
    },
    {
        "input": "test/data/TwoObstacles.yaml",
        "expected_path": [(2, 2), (10, 5), (70, 40), (98, 98)]
    },
    {
        "input": "test/data/OverlappingObstacles.yaml",
        "expected_path": [(2, 2), (25, 50), (35, 60), (98, 98)]  
    },
]

@pytest.mark.parametrize("test_case", test_cases_shortest_time)
def test_shortest_time(monkeypatch, test_case):
    # Mock command line arguments
    output_file = "test_output.txt"
    monkeypatch.setattr(sys, 'argv', ['main.py', test_case['input'], output_file, "-type", "time"])
    
    # Run the program
    main()

    path_output = []
    # Read the resulting output file
    with open(output_file, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            path_output.append((int(numbers[0]), int(numbers[1])))

    # Check if the path is correct
    assert len(path_output) == len(test_case['expected_path']), "Path length mismatch"
    for expected, actual in zip(test_case['expected_path'], path_output):
        assert expected == actual, f"Expected {expected}, but got {actual}"

    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)
