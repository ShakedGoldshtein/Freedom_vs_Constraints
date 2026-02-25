```python
def optimal_company_name(o_leg, i_gor):
    o_leg = sorted(o_leg)
    i_gor = sorted(i_gor, reverse=True)
    res = ['']*len(o_leg)
    beg, end = 0, len(o_leg) - 1
    o_turn = True
    while beg <= end:
        while beg <= end and (o_turn or o_leg[0] <= i_gor[0]):
            if res[beg] != '':
                break
            if o_leg[0] < i_gor[-1]:
                res[beg] = o_leg.pop(0)
            else:
                res[end] = o_leg.pop()
                end -= 1
            o_turn = not o_turn
        while beg <= end and (not o_turn or o_leg[0] >= i_gor[0]):
            if res[beg] != '':
                beg += 1
            else:
                res[end] = i_gor.pop(0)
                end -= 1
            o_turn = not o_turn
    return ''.join(res)
```