```python
_UNITS_BASE = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
_TEENS_BASE = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
_TENS_BASE = ["", "dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

def _get_polish_number_word(num: int) -> str:
    """Converts a number (1-99) to its Polish word representation for ordering beers."""
    if num == 1:
        return "Jedno"  # Special neuter form for "piwo"
    if 1 <= num <= 9:
        return _UNITS_BASE[num]
    elif 10 <= num <= 19:
        return _TEENS_BASE[num - 10]
    elif 20 <= num <= 99:
        tens_digit = num // 10
        units_digit = num % 10
        if units_digit == 0:
            return _TENS_BASE[tens_digit]
        else:
            return f"{_TENS_BASE[tens_digit]} {_UNITS_BASE[units_digit]}"
    return "" # Should not be reached given input constraints

def order_beers(num_beers: int) -> str:
    """
    Generates the Polish phrase for ordering a given number of beers.

    Args:
        num_beers: The number of beers to order (0-99).

    Returns:
        A string with the Polish order phrase.

    Raises:
        ValueError: If num_beers is outside the range 0-99.
    """
    if not (0 <= num_beers <= 99):
        raise ValueError("Number of beers must be between 0 and 99.")

    if num_beers == 0:
        return "Woda mineralna"

    number_word = _get_polish_number_word(num_beers)

    noun_form = ""
    if num_beers == 1:
        noun_form = "piwo"  # Nominative singular
    else:
        last_digit = num_beers % 10
        # Exception to the exception: 12, 13, 14 take genitive plural
        if num_beers in [12, 13, 14]:
            noun_form = "piw"  # Genitive plural
        # Numbers ending in 2, 3, 4 (excluding 12, 13, 14) take nominative plural
        elif last_digit in [2, 3, 4]:
            noun_form = "piwa"  # Nominative plural
        else:
            noun_form = "piw"  # Default is genitive plural

    return f"{number_word} {noun_form} poprosze"
```