```python
def solve(s: str, t: str) -> str:
    n = len(s)

    # Sort Oleg's letters in ascending order
    s_chars = sorted(list(s))
    # Sort Igor's letters in ascending order
    t_chars = sorted(list(t))

    # Calculate number of moves for each player
    # Oleg moves first, so he takes ceil(n/2) turns
    # Igor takes floor(n/2) turns
    k_o = (n + 1) // 2
    k_i = n // 2

    # Pointers for Oleg's available character pool
    # Oleg uses his k_o smallest characters
    s_p1 = 0  # Pointer to Oleg's current smallest available character
    s_p2 = k_o - 1  # Pointer to Oleg's current largest available character (from his designated k_o smallest)

    # Pointers for Igor's available character pool
    # Igor uses his k_i largest characters
    t_p1 = n - k_i  # Pointer to Igor's current smallest available character (from his designated k_i largest)
    t_p2 = n - 1    # Pointer to Igor's current largest available character

    # Initialize the company name as a list of characters
    ans = [''] * n
    ans_left = 0  # Pointer to the leftmost empty position in 'ans'
    ans_right = n - 1 # Pointer to the rightmost empty position in 'ans'

    for turn in range(n):
        if turn % 2 == 0:  # Oleg's turn
            # Oleg wants to make the string lexicographically as small as possible.
            # He considers placing his smallest available character (s_chars[s_p1]) at ans[ans_left].
            # Igor would try to counter with his largest available character (t_chars[t_p2]).

            # Check if Oleg's current best char is better than Igor's current best char
            # or if Igor has run out of his 'best' chars to counter effectively.
            if s_chars[s_p1] < t_chars[t_p2]:
                # Oleg can make a good move for an early position.
                ans[ans_left] = s_chars[s_p1]
                s_p1 += 1
                ans_left += 1
            else:
                # Oleg cannot guarantee making ans[ans_left] smaller than what Igor would force.
                # He must sacrifice an early position to preserve better characters for later turns,
                # or when Igor's options are limited.
                # He places his largest remaining character from his chosen pool at the latest possible position.
                ans[ans_right] = s_chars[s_p2]
                s_p2 -= 1
                ans_right -= 1
        else:  # Igor's turn
            # Igor wants to make the string lexicographically as large as possible.
            # He considers placing his largest available character (t_chars[t_p2]) at ans[ans_left].
            # Oleg would try to counter with his smallest available character (s_chars[s_p1]).

            # Check if Igor's current best char is better than Oleg's current best char
            # or if Oleg has run out of his 'best' chars to counter effectively.
            if t_chars[t_p2] > s_chars[s_p1]:
                # Igor can make a good move for an early position.
                ans[ans_left] = t_chars[t_p2]
                t_p2 -= 1
                ans_left += 1
            else:
                # Igor cannot guarantee making ans[ans_left] larger than what Oleg would force.
                # He must sacrifice an early position.
                # He places his smallest remaining character from his chosen pool at the latest possible position.
                ans[ans_right] = t_chars[t_p1]
                t_p1 += 1
                ans_right -= 1

    return "".join(ans)

```