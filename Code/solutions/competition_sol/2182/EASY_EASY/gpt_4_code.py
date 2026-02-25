```python
def define_company_name(s:str, t:str):
    n = len(s)

    s = sorted(s, reverse = True)
    t = sorted(t, reverse = False)

    comp_name = [0]*n

    l, r = 0, n-1
    flag = True

    for _ in range(n):
        if flag:
            if s[-1] < t[-1]:
                comp_name[l] = s.pop()
                l += 1
            else:
                if s[-1] > t[0]:
                    comp_name[r] = s.pop()
                    r -= 1
                else:
                    comp_name[l] = s.pop()
                    l += 1
        else:
            if t[0] > s[-1]:
                comp_name[r] = t.pop(0)
                r -= 1
            else:
                if t[0] < s[0]:
                    comp_name[l] = t.pop(0)
                    l += 1
                else:
                    comp_name[r] = t.pop(0)
                    r -= 1
        flag = not flag

    return ''.join(map(str, comp_name))
```
