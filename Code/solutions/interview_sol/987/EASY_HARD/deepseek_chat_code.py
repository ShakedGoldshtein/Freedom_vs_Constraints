```python
import math

def solve(finish, distancetoBolt, tigerAccelaration, boltSpeed):
    time_bolt = finish / boltSpeed
    
    discriminant = 2 * tigerAccelaration * (finish + distancetoBolt)
    if discriminant < 0:
        return "Tiger"
    
    time_tiger = math.sqrt(discriminant) / tigerAccelaration
    
    if time_bolt < time_tiger:
        return "Bolt"
    else:
        return "Tiger"

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        finish = int(input_data[index])
        distancetoBolt = int(input_data[index+1])
        tigerAccelaration = int(input_data[index+2])
        boltSpeed = int(input_data[index+3])
        index += 4
        result = solve(finish, distancetoBolt, tigerAccelaration, boltSpeed)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```