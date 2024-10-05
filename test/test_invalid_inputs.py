import pytest
from main import main
import sys


def test_invalid_object(monkeypatch):
    # Mock command line arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', 'test/data/InvalidObstacle.yaml'])

    # Run the main function
    with pytest.raises(Exception, match="Invalid yaml input: obstacle intersects itself"):
        main()

def test_no_path(monkeypatch):
    # Mock command line arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', 'test/data/NoPossiblePath.yaml'])

    # Run the main function
    with pytest.raises(Exception, match="No valid path from start to goal found"):
        main()
