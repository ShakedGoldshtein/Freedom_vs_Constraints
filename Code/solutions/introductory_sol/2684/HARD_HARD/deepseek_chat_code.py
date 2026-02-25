```python
def ordering_beers(n):
    if n < 0 or n > 99:
        raise ValueError("Number of beers must be between 0 and 99")
    
    if n == 0:
        return "Woda mineralna"
    
    number_word = _number_to_polish(n)
    beer_form = _get_beer_form(n)
    
    return f"{number_word} {beer_form} poprosze"

def _number_to_polish(n):
    if n == 0:
        return "zero"
    elif n == 1:
        return "Jedno"
    
    units = ["", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
    teens = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", 
             "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
    tens = ["", "", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", 
            "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
    
    if n < 10:
        return units[n].capitalize()
    elif n < 20:
        return teens[n - 10].capitalize()
    else:
        ten_part = tens[n // 10]
        unit_part = units[n % 10]
        if unit_part:
            return f"{ten_part} {unit_part}".capitalize()
        else:
            return ten_part.capitalize()

def _get_beer_form(n):
    if n == 1:
        return "piwo"
    
    last_two_digits = n % 100
    
    if 12 <= last_two_digits <= 14:
        return "piw"
    
    last_digit = n % 10
    if 2 <= last_digit <= 4:
        return "piwa"
    else:
        return "piw"
```