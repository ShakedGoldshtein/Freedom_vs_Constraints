```python
def riders(stations):
    riders = 1
    distance = 0
    for station in stations:
        if distance + station > 100:
            riders += 1
            distance = station
        else:
            distance += station
    return riders
```