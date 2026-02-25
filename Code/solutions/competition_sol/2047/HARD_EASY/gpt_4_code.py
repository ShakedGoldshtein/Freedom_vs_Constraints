```python
def solve_parking_problem(n, k, lot):
    cars = [None]*(k+1)
    park_spots = [None]*(k+1)
    for i in range(4):
        for j in range(n):
            if lot[i][j] > 0:
                if i < 2:
                    park_spots[lot[i][j]] = (i, j)
                else:
                    cars[lot[i][j]] = (i, j)

    # move directly parked cars
    moves = []
    for i in range(1, k+1):
        if park_spots[i][1] == cars[i][1]:
            if park_spots[i][0] < cars[i][0]:
                moves += [(i, r, park_spots[i][1]) for r in range(cars[i][0], park_spots[i][0], -1)]
            else:
                moves += [(i, r, park_spots[i][1]) for r in range(cars[i][0], park_spots[i][0] + 1)]
            cars[i] = None
    not_parked_cars = [i for i in range(1, k+1) if cars[i] is not None]
    if not not_parked_cars:
        return moves

    # find empty spot
    empty_spot = None
    for i in range(2, 4):
        for j in range(n):
            if lot[i][j] == 0:
                empty_spot = (i, j)
                break
    if empty_spot is None:
        return -1

    # try to park remaining cars using circular movement
    while not_parked_cars:
        cur_car = None
        for i in range(1, n+1):
            for j in range(2, 4):
                if cars[cur_car] == ((j+1)%2+2, i%n-1):
                    cars[cur_car] = empty_spot
                    if park_spots[cur_car] == cars[cur_car]:
                        not_parked_cars.remove(cur_car)
                cur_car = lot[j][i%n-1]
                if empty_spot == (j, i%n-1):
                    empty_spot = cars[cur_car]
                if cur_car:
                    moves.append((cur_car, j, i%n-1))
                    cars[cur_car] = (j, i%n-1)
                    if park_spots[cur_car] == cars[cur_car]:
                        not_parked_cars.remove(cur_car)
    return moves
```
