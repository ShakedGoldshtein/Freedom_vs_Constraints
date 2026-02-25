```python
def solve(s, k):
    n = len(s)
    all_chars = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s)
    
    if k == n:
        return ''.join(sorted(s))
    
    available = sorted(all_chars - s_set)
    s_sorted = sorted(s)
    
    def find_smallest(prefix, used_s, used_t, common_count):
        pos = len(prefix)
        if pos == n:
            return prefix
        
        for char in sorted(available + s_sorted):
            if char in used_t:
                continue
                
            new_common = common_count
            if char in used_s:
                new_common += 1
                
            if new_common > k:
                continue
                
            remaining = n - pos - 1
            max_possible_common = new_common + min(remaining, len(used_s & (set(available + s_sorted) - used_t - {char})))
            if max_possible_common > k:
                continue
                
            new_used_t = used_t | {char}
            new_used_s = used_s
            if char in s_set:
                new_used_s = used_s | {char}
                
            res = find_smallest(prefix + char, new_used_s, new_used_t, new_common)
            if res:
                return res
        return None
    
    result = find_smallest("", set(), set(), 0)
    return result if result else "NOPE"

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        parts = input_data[index].split()
        index += 1
        s = parts[0]
        k = int(parts[1])
        results.append(solve(s, k))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```