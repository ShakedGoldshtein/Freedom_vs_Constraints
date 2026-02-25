```python
from typing import List, Union

def calculate_lost_sheep(
    friday_counts: List[int],
    saturday_counts: List[int],
    total_sheep: int
) -> int:
    """
    Calculate the number of sheep lost after Friday and Saturday returns.

    Args:
        friday_counts: List of sheep counts returned on Friday night.
        saturday_counts: List of sheep counts returned on Saturday night.
        total_sheep: Total number of sheep the farmer originally had.

    Returns:
        The number of sheep lost (non-negative integer).

    Raises:
        ValueError: If any input is invalid (negative counts, empty lists, or total_sheep too small).
    """
    def _validate_counts(counts: List[int], day_name: str) -> None:
        if not counts:
            raise ValueError(f"{day_name} counts list cannot be empty")
        if any(count <= 0 for count in counts):
            raise ValueError(f"All {day_name} counts must be positive integers")

    _validate_counts(friday_counts, "Friday")
    _validate_counts(saturday_counts, "Saturday")

    total_returned = sum(friday_counts) + sum(saturday_counts)

    if total_returned > total_sheep:
        raise ValueError("Total returned sheep cannot exceed original total")

    return total_sheep - total_returned
```