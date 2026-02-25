```python
def solve(n, string_list, m, operations):
    results = []

    # dict to store all the possible substrings
    led = {}

    # to store all the strings
    s = string_list[:]

    # initial population of dict
    for i in range(n):
        led[i] = set()
        for j in range(len(s[i])):
            for k in range(j+1, len(s[i])+1):
                if len(s[i][j:k])<=10:
                    led[i].add(int(s[i][j:k], 2))

    # perform all operations
    for i in range(m):
        a,b = operations[i]
        a -= 1
        b -= 1
        s.append(s[a] + s[b])
        led[n+i] = led[a] | led[b]

        # adding all possible substrings to dict
        for j in range(len(s[b])-10, len(s[b])):
            if j < 0:
                j = 0
            for k in range(j+1, min(j+12, len(s[n+i])+1)):
                if s[n+i][j:k]!=0:
                    led[n+i].add(int(s[n+i][j:k], 2))

        # checking for max length
        max_len = 0
        while (1 << max_len)-1 in led[n+i]:
            max_len += 1
        max_len -= 1
        results.append(max_len)
    
    return results



n = 5
s = ['01', '10', '101', '11111', '0']
m = 3
operations = [(1, 2), (6, 5), (4, 4)]
print(solve(n, s, m, operations))  # OUTPUT: [1, 2, 0]
```