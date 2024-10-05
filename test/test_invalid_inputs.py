import pytest
import numpy as np
from main import main
import yaml
import sys
from io import StringIO

# Test cases and their expected outputs
test_cases = [
    {
        "input": "test/data/InvalidObstacle.yaml",
        "expected_path": [(2, 2), (10.0, 5.0), (20.0, 15.0), (60.0, 80.0), (80.0, 90.0), (98, 98)]  
    }
]

@pytest.mark.parametrize("test_case", test_cases)
def test_main(monkeypatch, test_case):
    # Mock command line arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', test_case['input']])
    
    # Capture the output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    # Run the main function
    with pytest.raises(Exception, match="Invalid yaml input: obstacle intersects itself"):
        main()

