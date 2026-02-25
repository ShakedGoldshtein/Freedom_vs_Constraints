```python
def solve_test_case(n):
    if n % 2 == 0:
        return '1' * (n // 2)
    else:
        return '7' + '1' * ((n - 3) // 2)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve_test_case(n))

if __name__ == "__main__":
    main()
```