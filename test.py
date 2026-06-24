"""Colour Validator Tests"""
import subprocess
import sys
from colour_validator import ColourValidator


def test_colour_validator_init():
    """Test the initialization of the ColourValidator class."""
    validator = ColourValidator("red")
    assert validator.colour == "red"

def test_colour_validator_get_colour():
    """Test the get_colour method of the ColourValidator class."""
    validator = ColourValidator("red")
    assert validator.get_colour() == "The colour is red."

    validator = ColourValidator("invalid")
    assert validator.get_colour() == "The colour is not in the list."

def test_colour_validator_run(capsys):
    """Test the run method of the ColourValidator class."""
    validator = ColourValidator("blue")
    validator.run()
    captured = capsys.readouterr()
    assert captured.out == "The colour is blue.\n"
