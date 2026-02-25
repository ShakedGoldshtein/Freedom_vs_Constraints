```python
def orderingBeers(n):
    if not isinstance(n, int) or n < 0 or n > 99:
        raise ValueError("Number must be an integer between 0 and 99")
        
    if n == 0:
        return "Woda mineralna"
        
    if n == 1:
        return "Jedno piwo poprosze"
        
    units = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", 
             "siedem", "osiem", "dziewiec"]
             
    teens = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie",
             "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
             
    tens = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat",
            "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

    def get_number_text(n):
        if n < 10:
            return units[n]
        elif n < 20:
            return teens[n-10]
        else:
            t, u = divmod(n, 10)
            if u == 0:
                return tens[t-1]
            return f"{tens[t-1]} {units[u]}"
            
    def get_beer_form(n):
        if 12 <= n <= 14:
            return "piw"
        elif n % 10 in [2,3,4] and n not in [12,13,14]:
            return "piwa"
        return "piw"
        
    return f"{get_number_text(n)} {get_beer_form(n)} poprosze"
```