```python
def solve(n: int) -> list[int]:
    """
    Determines the minimum number of questions Petya needs to ask to guarantee guessing Vasya's number.

    Args:
        n (int): The upper limit of the range of numbers Vasya can think of (1 ≤ n ≤ 10^3).

    Returns:
        list[int]: A list containing the number of questions followed by the sequence of questions.
                  The first element is the count of questions, and the rest are the questions themselves.
    """
    # Handle edge cases where n is 1 or 2
    if n == 1:
        return [0]  # No questions needed if there's only one possible number
    if n == 2:
        return [1, 2]  # Only one question needed to distinguish between 1 and 2

    # Initialize the list of questions with the first two questions: 2 and n
    questions = [2, n]

    # Add odd numbers greater than 2 to the list of questions
    for i in range(3, n + 1, 2):
        questions.append(i)

    # Return the result: the count of questions followed by the questions themselves
    return [len(questions)] + questions
```