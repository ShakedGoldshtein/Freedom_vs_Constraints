```python
class _PolishNumerals:
    """
    Helper class for generating Polish number words and determining noun forms.
    Not intended for direct instantiation.
    """
    _UNITS_WORDS = [
        "zero", "jeden", "dwa", "trzy", "cztery",
        "piec", "szesc", "siedem", "osiem", "dziewiec"
    ]
    _TEENS_WORDS = [ # For numbers 10-19
        "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie",
        "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"
    ]
    _TENS_WORDS = [ # For tens multiples (0, 10, 20, ..., 90)
        "", "dziesiec", "dwadziescia", "trzydziesci", "czterdziesci",
        "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"
    ]

    @staticmethod
    def get_polish_number_string(num: int) -> str:
        """
        Converts an integer (0-99) to its Polish word representation.

        For the number 1, it returns "jeden" (masculine/generic form), not "jedno"
        (neuter form), as "jedno" is a specific grammatical case for neuter nouns
        like "piwo" when ordering a single item, and is handled separately by the
        main `order_beers` function for `num_beers = 1`.

        Args:
            num: An integer between 0 and 99, inclusive.

        Returns:
            A string with the Polish word representation of the number.
        """
        if num == 0:
            return _PolishNumerals._UNITS_WORDS[0]
        elif num < 10:
            return _PolishNumerals._UNITS_WORDS[num]
        elif num < 20: # Numbers from 10 to 19
            return _PolishNumerals._TEENS_WORDS[num - 10]
        else: # Numbers from 20 to 99
            tens_digit = num // 10
            units_digit = num % 10
            result = _PolishNumerals._TENS_WORDS[tens_digit]
            if units_digit > 0:
                result += " " + _PolishNumerals._UNITS_WORDS[units_digit]
            return result

    @staticmethod
    def get_noun_form_for_beers(num: int) -> str:
        """
        Determines the correct Polish noun form for 'beer' (piwo) based on the number.

        This function applies Polish grammar rules for number-noun agreement for "piwo".
        It assumes `num` is greater than 1, as the `num_beers = 1` case is handled
        specifically in the `order_beers` function.

        Args:
            num: An integer greater than 1, representing the number of beers.

        Returns:
            A string: "piw" (genitive plural) or "piwa" (nominative plural).
        """
        # Exception to the exception: for 12, 13 and 14, it's genitive plural ("piw").
        # This rule actually applies to all numbers from 10 to 19 because they are
        # treated as a distinct group for noun agreement.
        if 10 <= num % 100 <= 19:
            return "piw"

        # Rule: after the numerals 2, 3, 4, and compound numbers ending with them
        # (e.g., 22, 23, 24), the noun takes nominative plural ("piwa").
        last_digit = num % 10
        if last_digit in [2, 3, 4]:
            return "piwa"
        
        # Default rule: usually the plural is genitive ("piw"). This covers numbers
        # ending with 0, 1, 5, 6, 7, 8, 9 (excluding the 10-19 range already handled).
        return "piw"


def order_beers(num_beers: int) -> str:
    """
    Generates the Polish phrase for ordering a specified number of beers.

    This function handles input validation, special cases for zero and one beer,
    and applies Polish grammar rules for number-noun agreement (cases) for "piwo"
    (beer). It constructs the correct Polish string for ordering.

    Args:
        num_beers: An integer representing the number of beers to order.
                   Must be between 0 and 99, inclusive.

    Returns:
        A string containing the correct Polish phrase.

    Raises:
        ValueError: If `num_beers` is outside the supported range [0, 99].

    Optimal Time Complexity: O(1)
        The number of operations (lookups in constant-size lists, arithmetic,
        and string concatenations) is constant regardless of the input number,
        as the maximum number of digits and words involved is fixed.

    Optimal Space Complexity: O(1)
        The space used for storing word lists and constructing the output string
        is constant, not scaling with the input number.
    """
    if not (0 <= num_beers <= 99):
        raise ValueError("Number of beers must be between 0 and 99, inclusive.")

    if num_beers == 0:
        return "Woda mineralna"
    elif num_beers == 1:
        # Special case for "one beer" using the neuter form "Jedno" for "piwo"
        return "Jedno piwo poprosze"
    else:
        # Get the Polish word for the number (e.g., "dwa", "dwadziescia dwa")
        polish_num_str = _PolishNumerals.get_polish_number_string(num_beers)
        
        # Get the correct grammatical form of "beer" (piwa or piw)
        noun_form = _PolishNumerals.get_noun_form_for_beers(num_beers)
        
        # Combine the number, noun, and the request phrase
        return f"{polish_num_str} {noun_form} poprosze"
```