```python
def generate_string(s, k):
    n = len(s)
    all_chars = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s)
    
    def find_lex_smallest():
        if k == n:
            return ''.join(sorted(s))
        
        available = sorted(all_chars - s_set)
        required_diff = n - k
        
        result = []
        used_from_s = set()
        used_from_available = set()
        
        for i in range(n):
            for char in sorted(s_set - used_from_s | set(available) - used_from_available):
                temp_result = result + [char]
                remaining_positions = n - len(temp_result)
                
                max_possible_s_chars = 0
                remaining_s_chars = s_set - used_from_s
                if char in remaining_s_chars:
                    remaining_s_chars_after = remaining_s_chars - {char}
                    max_possible_s_chars = 1 + min(len(remaining_s_chars_after), remaining_positions)
                else:
                    max_possible_s_chars = min(len(remaining_s_chars), remaining_positions)
                
                current_s_chars = len(used_from_s) + (1 if char in s_set and char not in used_from_s else 0)
                min_forced_s_chars = current_s_chars + max(0, len(remaining_s_chars) - len(available - used_from_available - set(remaining_s_chars)))
                
                if min_forced_s_chars <= k and current_s_chars + max_possible_s_chars <= k + remaining_positions:
                    result.append(char)
                    if char in s_set:
                        used_from_s.add(char)
                    else:
                        used_from_available.add(char)
                    break
            else:
                return None
        
        return ''.join(result) if len(result) == n else None
    
    res = find_lex_smallest()
    return res if res is not None else "NOPE"

def solve(input_data):
    lines = input_data.strip().split('\n')
    t = int(lines[0])
    results = []
    
    for i in range(1, t + 1):
        parts = lines[i].split()
        s = parts[0]
        k = int(parts[1])
        results.append(generate_string(s, k))
    
    return '\n'.join(results)
```