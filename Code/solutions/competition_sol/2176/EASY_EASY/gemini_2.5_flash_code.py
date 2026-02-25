```python
import heapq

MOD = 10**9 + 7
MAX_PRICE_PLUS_1 = 308983067 # Max price is 308983066, so +1 for infinity-like bound

class OrderBookSolver:
    def __init__(self):
        self.buy_heap = []  # Max-heap for confirmed BUY orders (store -price)
        self.sell_heap = [] # Min-heap for confirmed SELL orders (store price)

        # Heaps for undecided orders, allowing efficient min/max access with lazy deletion
        # undecided_lower: max-heap, stores -price of undecided orders
        # undecided_upper: min-heap, stores price of undecided orders
        self.undecided_lower = []
        self.undecided_upper = []
        # undecided_set: dict to track presence for O(1) removal check for lazy deletion
        self.undecided_set = {} # price -> True

        self.num_ways = 1

    # Helper to get current fixed bounds from confirmed orders
    def _get_fixed_bounds(self):
        bb_fixed = -self.buy_heap[0] if self.buy_heap else 0
        bs_fixed = self.sell_heap[0] if self.sell_heap else MAX_PRICE_PLUS_1
        return bb_fixed, bs_fixed

    # Helper for lazy deletion: removes elements from heap that are no longer in undecided_set
    def _clean_heap(self, heap, is_lower_heap):
        if is_lower_heap: # Max-heap, stores -price
            while heap and -heap[0] not in self.undecided_set:
                heapq.heappop(heap)
        else: # Min-heap, stores price
            while heap and heap[0] not in self.undecided_set:
                heapq.heappop(heap)

    # Helper to get current min/max of undecided orders (considering lazy deletion)
    def _get_undecided_min_max(self):
        self._clean_heap(self.undecided_lower, True)
        self._clean_heap(self.undecided_upper, False)
        
        max_u = -self.undecided_lower[0] if self.undecided_lower else 0
        min_u = self.undecided_upper[0] if self.undecided_upper else MAX_PRICE_PLUS_1
        return min_u, max_u

    def add_order(self, p):
        if self.num_ways == 0: return

        bb_fixed, bs_fixed = self._get_fixed_bounds()
        min_u, max_u = self._get_undecided_min_max()

        # Effective bounds combine fixed and current undecided extremes
        effective_bb = max(bb_fixed, max_u)
        effective_bs = min(bs_fixed, min_u)

        if p < effective_bb:
            heapq.heappush(self.buy_heap, -p)
        elif p > effective_bs:
            heapq.heappush(self.sell_heap, p)
        elif effective_bb < p < effective_bs:
            # If p falls strictly within the current effective undecided range, it itself becomes undecided.
            heapq.heappush(self.undecided_lower, -p)
            heapq.heappush(self.undecided_upper, p)
            self.undecided_set[p] = True
        else: # p == effective_bb or p == effective_bs or effective_bb >= effective_bs (inconsistent state)
            self.num_ways = 0
            return

        # Check for immediate inconsistency after adding this order
        final_bb_fixed, final_bs_fixed = self._get_fixed_bounds()
        final_min_u, final_max_u = self._get_undecided_min_max()
        if max(final_bb_fixed, final_max_u) >= min(final_bs_fixed, final_min_u):
            self.num_ways = 0

    def accept_order(self, p):
        if self.num_ways == 0: return

        bb_fixed, bs_fixed = self._get_fixed_bounds()
        min_u, max_u = self._get_undecided_min_max()

        # Determine if p can be accepted from fixed heaps or undecided set
        can_accept_as_fixed_buy = (self.buy_heap and p == -self.buy_heap[0])
        can_accept_as_fixed_sell = (self.sell_heap and p == self.sell_heap[0])
        is_p_undecided = (p in self.undecided_set)
        
        ways_to_accept_p = 0

        # Case 1: p is from fixed BUY/SELL orders
        if can_accept_as_fixed_buy and can_accept_as_fixed_sell:
            ways_to_accept_p = 2
        elif can_accept_as_fixed_buy or can_accept_as_fixed_sell:
            ways_to_accept_p = 1
        
        # Case 2: p is an undecided order
        if is_p_undecided:
            # p must be either the effective best BUY or effective best SELL from undecided orders
            
            # If p is the only undecided order, it can potentially be accepted as either BUY or SELL
            if p == min_u and p == max_u:
                if not can_accept_as_fixed_buy and p > bb_fixed: # Can be accepted as BUY
                    ways_to_accept_p += 1
                if not can_accept_as_fixed_sell and p < bs_fixed: # Can be accepted as SELL
                    ways_to_accept_p += 1
            elif p == max_u: # p is the highest undecided, can only be accepted as BUY
                if not can_accept_as_fixed_buy and p > bb_fixed:
                    ways_to_accept_p += 1
            elif p == min_u: # p is the lowest undecided, can only be accepted as SELL
                if not can_accept_as_fixed_sell and p < bs_fixed:
                    ways_to_accept_p += 1
            else: # p is in undecided but not min_u/max_u, so it cannot be accepted
                self.num_ways = 0
                return
        
        if ways_to_accept_p == 0:
            self.num_ways = 0
            return

        if ways_to_accept_p == 2:
            self.num_ways = (self.num_ways * 2) % MOD
        
        # Remove p from its respective structure(s)
        if can_accept_as_fixed_buy:
            heapq.heappop(self.buy_heap)
        if can_accept_as_fixed_sell:
            heapq.heappop(self.sell_heap)
        
        if is_p_undecided:
            # When an undecided order `p` is accepted, all *other* currently undecided orders
            # are forced to be either BUY (if < p) or SELL (if > p).
            # This means the current `undecided_set` effectively becomes resolved.
            
            # Mark p as removed from undecided
            self.undecided_set.pop(p) 

            # Move all remaining elements from undecided_set to confirmed heaps
            # Elements < p become BUYs, elements > p become SELLs.
            # Lazy deletion already handles emptying the heaps for logically removed items.
            # We iterate through undecided_set.keys() and move valid items.
            
            # Create a copy of keys to iterate, as we modify undecided_set
            undecided_vals_to_move = list(self.undecided_set.keys()) 
            
            for val in undecided_vals_to_move:
                if val < p:
                    heapq.heappush(self.buy_heap, -val)
                else: # val > p
                    heapq.heappush(self.sell_heap, val)
                self.undecided_set.pop(val) # Remove from set as it's now confirmed

            # Clear heaps as they will only contain removed elements logically
            self.undecided_lower.clear()
            self.undecided_upper.clear()

        # Final consistency check after accepting
        final_bb_fixed, final_bs_fixed = self._get_fixed_bounds()
        final_min_u, final_max_u = self._get_undecided_min_max()
        if max(final_bb_fixed, final_max_u) >= min(final_bs_fixed, final_min_u):
            self.num_ways = 0


def solve(n, actions_raw):
    # actions_raw is a list of lists/tuples, e.g., [["ADD", 1], ["ACCEPT", 1]]
    # Convert to appropriate format for OrderBookSolver (string, int)
    actions = []
    for action_str, p_val in actions_raw:
        actions.append((action_str, p_val))

    solver = OrderBookSolver()
    for action_type, p in actions:
        if solver.num_ways == 0: # If it's already impossible, no need to continue
            return 0
        
        if action_type == "ADD":
            solver.add_order(p)
        elif action_type == "ACCEPT":
            solver.accept_order(p)
    
    if solver.num_ways == 0:
        return 0

    # Final step: any remaining undecided orders contribute (len + 1) ways
    solver._clean_heap(solver.undecided_lower, True)
    solver._clean_heap(solver.undecided_upper, False)
    
    if solver.undecided_set:
        # Check for final inconsistency before multiplying
        final_bb_fixed, final_bs_fixed = solver._get_fixed_bounds()
        final_min_u, final_max_u = solver._get_undecided_min_max()
        if max(final_bb_fixed, final_max_u) >= min(final_bs_fixed, final_min_u):
            return 0
        
        solver.num_ways = (solver.num_ways * (len(solver.undecided_set) + 1)) % MOD
    
    return solver.num_ways

```