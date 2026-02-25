```python
def _is_contest_balanced(num_problems: int, num_participants: int, problem_solvers: list[int]) -> bool:
    """
    Determines if a single contest is balanced according to Chef's rules.

    A contest is balanced if it has exactly 1 cakewalk problem and exactly 2 hard problems.
    A problem is 'cakewalk' if it's solved by at least P/2 (integer division) participants.
    A problem is 'hard' if it's solved by at most P/10 (integer division) participants.

    Args:
        num_problems: The number of problems in the contest.
        num_participants: The total number of participants in the contest.
        problem_solvers: A list of integers, where each integer is the count of
                         participants who solved a specific problem.

    Returns:
        True if the contest is balanced, False otherwise.
    """
    cakewalk_threshold = num_participants // 2
    hard_threshold = num_participants // 10

    cakewalk_count = 0
    hard_count = 0

    for solvers_count in problem_solvers:
        if solvers_count >= cakewalk_threshold:
            cakewalk_count += 1
        if solvers_count <= hard_threshold:
            hard_count += 1

    return cakewalk_count == 1 and hard_count == 2


def determine_contest_balance(contest_data: list[tuple[int, int, list[int]]]) -> list[str]:
    """
    Processes multiple contest descriptions to determine if each contest was balanced.

    This function adheres to the critical requirements:
    - It's a single function accepting all input as parameters.
    - It returns the result without using any I/O operations.
    - It processes multiple test cases as per the problem description.

    Args:
        contest_data: A list of test cases. Each test case is represented as a tuple:
                      (N, P, problem_solvers_list), where:
                      - N (int): The number of problems in the contest.
                      - P (int): The total number of participants in the contest.
                      - problem_solvers_list (list[int]): A list of N integers,
                                                          denoting the number of participants
                                                          solving each problem.

    Returns:
        A list of strings ("yes" or "no"), where each string corresponds to whether
        the respective contest in `contest_data` was balanced.
    """
    results = []
    for N, P, problem_solvers in contest_data:
        if _is_contest_balanced(N, P, problem_solvers):
            results.append("yes")
        else:
            results.append("no")
    return results
```