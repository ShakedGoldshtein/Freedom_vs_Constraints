```python
from collections import defaultdict
def solve(k, boxes_contents):
    total_sum, box_index, prefix_sum, boxes, memo, combos = 0, {}, [], [], {}, []
    
    for i, box in enumerate(boxes_contents):
        boxes.append(box)
        prefix_sum.append(total_sum)
        for value in box:
            total_sum += value
            box_index[value] = i
    
    if total_sum % k != 0:
        return ["No"]
    else:
        target_sum = total_sum // k
        
    def dfs(current_box, current_sum, used_boxes, combo):
        
        if used_boxes in memo:
            return memo[used_boxes]
        
        if current_sum == target_sum:
            combos.append(combo)
            return used_boxes
        
        for value in boxes[current_box]:
            
            if used_boxes & (1 << current_box):
                continue
            
            next_box = box_index[target_sum - current_sum + value]
            
            if used_boxes & (1<<next_box):
                continue
            
            used_boxes = dfs(next_box, current_sum - value, used_boxes | 1 << current_box, combo + [[value, next_box+1]])
            
            if used_boxes == ((1 << k) - 1):
                return used_boxes
            
            memo[used_boxes] = used_boxes
        return used_boxes
    
    used_boxes = dfs(0, target_sum, 0, [])
    
    if used_boxes != ((1 << k) - 1):
        return ["No"]
    
    else:
        result = ["Yes"]
        for i in range(k):
            result.append(combos[0][i])
            
    return result
```