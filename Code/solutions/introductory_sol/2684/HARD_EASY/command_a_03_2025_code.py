```python
def ordering_beers(n: int) -> str:
    """
    Returns the Polish phrase for ordering beers based on the number of beers.

    Args:
        n (int): The number of beers to order. Must be between 0 and 99.

    Returns:
        str: The Polish phrase for ordering the specified number of beers.

    Raises:
        ValueError: If the number of beers is outside the range 0-99.
    """
    if not 0 <= n <= 99:
        raise ValueError("Number of beers must be between 0 and 99")

    if n == 0:
        return "Woda mineralna"

    units = [
        "", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"
    ]
    teens = [
        "dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie",
        "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"
    ]
    tens = [
        "", "dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat",
        "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"
    ]

    def polish_number(num: int) -> str:
        """
        Converts a number to its Polish representation.

        Args:
            num (int): The number to convert. Must be between 0 and 99.

        Returns:
            str: The Polish representation of the number.
        """
        if num < 10:
            return units[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        else:
            ten, unit = divmod(num, 10)
            return f"{tens[ten]} {units[unit]}" if unit != 0 else tens[ten]

    beer_form = "piwo" if n == 1 else ("piwa" if n in [2, 3, 4] and n not in [12, 13, 14] else "piw")
    return f"{polish_number(n).capitalize() if n == 1 else polish_number(n)} {beer_form} poprosze"
```