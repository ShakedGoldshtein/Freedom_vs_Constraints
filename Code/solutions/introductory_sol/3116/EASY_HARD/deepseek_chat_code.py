```python
def cal_n_bug(head, leg, wing_pair):
    # Let s = spiders, b = butterflies, d = dragonflies
    # Equations:
    # s + b + d = head
    # 8s + 6b + 6d = leg
    # 0s + 1b + 2d = wing_pair
    
    # From first equation: b + d = head - s
    # Substitute into second: 8s + 6(head - s) = leg
    # 8s + 6head - 6s = leg
    # 2s = leg - 6head
    # s = (leg - 6head) / 2
    
    if (leg - 6 * head) % 2 != 0:
        return [-1, -1, -1]
    
    s = (leg - 6 * head) // 2
    b_plus_d = head - s
    
    # From third equation: b + 2d = wing_pair
    # And we know: b + d = b_plus_d
    # Subtract: d = wing_pair - b_plus_d
    # Then: b = b_plus_d - d
    
    d = wing_pair - b_plus_d
    b = b_plus_d - d
    
    # Check if all are non-negative integers and satisfy all equations
    if s >= 0 and b >= 0 and d >= 0 and (s + b + d == head) and (8*s + 6*b + 6*d == leg) and (b + 2*d == wing_pair):
        return [s, b, d]
    else:
        return [-1, -1, -1]
```