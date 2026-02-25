```python
def solve(T, data):
    for i in range(T):
        N, M = map(int, data[i].split())
        if M < N-1 or M > N*(N-1)//2:
            print("-1 -1")
        elif N == 1:
            print("1 1")
        else:
            extra_edges = M - (N - 1)
            for j in range(1, N + 1):
                if j == N:
                    if extra_edges > 0:
                        print("{} {}".format(j, 1))
                        extra_edges -= 1
                    else:
                        print("{} {}".format(j, j - 1))
                else:
                    print("{} {}".format(j, j + 1))
            c1, c2 = 2, 3
            while extra_edges > 0:
                print("{} {}".format(c1, c2))
                extra_edges -= 1
                c1, c2 = c2, c2 % N + 1

solve(2, ['10 1', '5 5'])
```
This code was written with the Python programming language. It listens for the number of test cases and then tests each case separately. If the number of connections is less than the number of computers minus one, or if it is more than the number of ways to choose two computers out of all computers, it considers the task impossible and outputs "-1 -1". If there is only one computer, it outputs "1 1". If there are more than one computers, it connects each computer with the one next to it (the last one connects back to the first one). If there is a surplus of connections, they will connect the second computer with the third, then the third with the fourth, etc., until all connections are exhausted. The code returns the appropriate output for the given computer network requirements in the form of test outputs.