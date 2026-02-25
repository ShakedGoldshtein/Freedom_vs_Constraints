```python
def ordering_beers(n: int) -> str:
    """
    Returns the Polish phrase for ordering beers based on the number of beers requested.

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
    if n == 1:
        return "Jedno piwo poprosze"

    # Define Polish numbers
    units = [
        "",
        "jeden",
        "dwa",
        "trzy",
        "cztery",
        "piec",
        "szesc",
        "siedem",
        "osiem",
        "dziewiec",
    ]
    teens = [
        "dziesiec",
        "jedenascie",
        "dwanascie",
        "trzynascie",
        "czternascie",
        "pietnascie",
        "szesnascie",
        "siedemnascie",
        "osiemnascie",
        "dziewietnascie",
    ]
    tens = [
        "",
        "dziesiec",
        "dwadziescia",
        "trzydziesci",
        "czterdziesci",
        "piecdziesiat",
        "szescdziesiat",
        "siedemdziesiat",
        "osiemdziesiat",
        "dziewiecdziesiat",
    ]

    # Determine the beer form based on Polish grammar rules
    def get_beer_form(num: int) -> str:
        if num in [2, 3, 4] or (
            num > 10 and num < 20 and num - 10 in [2, 3, 4]
        ):  # 12, 13, 14
            return "piwa"
        else:
            return "piw"

    # Construct the Polish number phrase
    def get_number_phrase(num: int) -> str:
        if num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        else:
            t, u = divmod(num, 10)
            if u == 0:
                return tens[t]
            else:
                return f"{tens[t]} {units[u]}"

    beer_form = get_beer_form(n)
    number_phrase = get_number_phrase(n)
    return f"{number_phrase.capitalize()} {beer_form} poprosze"
```