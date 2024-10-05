import pytest
import numpy as np
from main import main
import yaml
import sys
from io import StringIO

# Test cases and their expected outputs
test_cases = [
    {
        "input": "test/data/NoObstacles.yaml",
        "expected_path": [(2, 2), (98, 98)]  
    },
    {
        "input": "test/data/ObstacleOutsideBounds.yaml",
        "expected_path": [(2, 2), (10.0, 5.0), (20.0, 15.0), (60.0, 80.0), (80.0, 90.0), (98, 98)]  
    },
    {
        "input": "test/data/NoPossiblePath.yaml",
        "expected_path": []  
    },
]

@pytest.mark.parametrize("test_case", test_cases)
def test_main(monkeypatch, test_case):
    # Mock command line arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', test_case['input']])
    
    # Capture the output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    # Run the main function
    main()

    # Get the printed output
    output = captured_output.getvalue()
    
    # Check if the path is printed correctly
    # (You might need to parse the output if you are printing more than just the path)
    lines = output.splitlines()
    path_str = next((line for line in lines if line.startswith('[')), None)
    
    if path_str:
        # Convert the output string to a list of tuples
        path_output = eval(path_str)
        assert len(path_output) == len(test_case['expected_path']), "Path length mismatch"
        for expected, actual in zip(test_case['expected_path'], path_output):
            assert np.allclose(expected, actual), f"Expected {expected}, but got {actual}"
    else:
        assert False, "No path output found"



