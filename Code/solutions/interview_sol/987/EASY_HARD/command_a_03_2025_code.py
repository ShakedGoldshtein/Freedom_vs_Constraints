```python
import math


def solve(finish: int, distancetoBolt: int, tigerAccelaration: int, boltSpeed: int) -> str:
    """
    Determines the winner of a race between Usain Bolt and a tiger.

    Args:
        finish (int): The distance to the finishing line from Bolt's starting position.
        distancetoBolt (int): The initial distance between the tiger and Bolt.
        tigerAccelaration (int): The acceleration of the tiger in m/s^2.
        boltSpeed (int): The constant speed of Bolt in m/s.

    Returns:
        str: "Bolt" if Bolt wins, "Tiger" otherwise.
    """
    # Calculate the time it takes for Bolt to reach the finish line
    bolt_time = finish / boltSpeed

    # Calculate the distance the tiger covers in the same time using the displacement formula
    tiger_distance = 0.5 * tigerAccelaration * (bolt_time**2)

    # Determine if the tiger reaches or surpasses the finish line before Bolt
    if tiger_distance > finish + distancetoBolt:
        return "Bolt"
    else:
        return "Tiger"


def main() -> None:
    """
    Main function to handle multiple test cases.
    Reads input, processes each test case, and prints the result.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    T = int(data[0])  # Number of test cases
    index = 1
    results: list[str] = []
    for _ in range(T):
        finish = int(data[index])
        distancetoBolt = int(data[index + 1])
        tigerAccelaration = int(data[index + 2])
        boltSpeed = int(data[index + 3])
        index += 4
        result = solve(finish, distancetoBolt, tigerAccelaration, boltSpeed)
        results.append(result)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```