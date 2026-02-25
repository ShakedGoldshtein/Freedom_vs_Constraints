```python
def solve_transform_binary_strings(test_cases):
    results = []
    for case in test_cases:
        n, a, b = case
        operations = []
        current = list(a)

        for i in range(n):
            if current[i] != b[i]:
                operations.append(i + 1)
                # Flip and reverse the prefix of length i+1
                prefix = current[:i+1]
                flipped = ['1' if bit == '0' else '0' for bit in prefix]
                reversed_flipped = flipped[::-1]
                current = reversed_flipped + current[i+1:]

        # Verify if the transformation is complete
        if ''.join(current) == b:
            results.append((len(operations), operations))
        else:
            # If not, perform a full flip to reset and try again
            operations.append(n)
            current = list(a)
            for i in range(n):
                if current[i] != b[i]:
                    operations.append(i + 1)
                    prefix = current[:i+1]
                    flipped = ['1' if bit == '0' else '0' for bit in prefix]
                    reversed_flipped = flipped[::-1]
                    current = reversed_flipped + current[i+1:]
            results.append((len(operations), operations))

    return results

def parse_input(test_cases_data):
    t = test_cases_data[0]
    index = 1
    test_cases = []
    for _ in range(t):
        n = test_cases_data[index]
        a = test_cases_data[index + 1]
        b = test_cases_data[index + 2]
        test_cases.append((n, a, b))
        index += 3
    return test_cases

def transform_binary_strings(test_cases_data):
    test_cases = parse_input(test_cases_data)
    results = solve_transform_binary_strings(test_cases)
    output = []
    for res in results:
        k, ops = res
        output.append([k] + ops)
    return output
```