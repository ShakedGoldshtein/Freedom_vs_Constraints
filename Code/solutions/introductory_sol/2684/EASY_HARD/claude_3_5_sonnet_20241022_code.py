```python
def ordering_beers(n):
    if not isinstance(n, int) or n < 0 or n > 99:
        raise ValueError("Number must be between 0 and 99")
        
    if n == 0:
        return "Woda mineralna"
        
    units = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
    teens = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"] 
    tens = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

    if n == 1:
        return "Jedno piwo poprosze"
        
    number = ""
    if n < 10:
        number = units[n]
    elif n < 20:
        number = teens[n-10]
    else:
        tens_digit = n // 10
        units_digit = n % 10
        number = tens[tens_digit-1]
        if units_digit > 0:
            number += " " + units[units_digit]

    piwo = "piw"
    if n in [2,3,4] or (n > 20 and n % 10 in [2,3,4] and n % 100 not in [12,13,14]):
        piwo = "piwa"
        
    return f"{number} {piwo} poprosze"
```