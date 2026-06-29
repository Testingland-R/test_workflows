"""colour_validator.py - Colour Validator for checking valid flavours."""


class ColourValidator:
    """Colour validator for checking valid colours."""

    VALID_COLOURS = {"red", "green", "blue", "yellow", "pink", "purple"}

    def __init__(self, colour: str):
        """Initialize the colour validator."""
        self.colour = colour

    def get_colour(self) -> str:
        """Get the colour of the colour validator."""
        if self.colour in self.VALID_COLOURS:
            return f"The colour is {self.colour}."
        return "The colour is not in the list."

    def run(self):
        """Run the main logic of the project."""
        print(self.get_colour())
