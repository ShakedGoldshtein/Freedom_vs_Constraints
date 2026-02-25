# Guidance texts for writing code

CREATE_GUIDANCE_HARD = """Write a production-grade solution to the following problem with optimal time and space complexity (Big-O). Produce clean, readable, and as-generic-as-possible code, organized into small, well-defined functions, with concise documentation but without unit testing or asserts. Ensure full correctness with comprehensive edge-case coverage, clear error handling, and prefer no unnecessary third-party dependencies.

CRITICAL REQUIREMENTS:
1. Your solution MUST be a function that takes input parameters and returns the output
2. DO NOT use stdin/stdout, input(), print(), or sys.stdin/sys.stdout
3. DO NOT use any I/O operations
4. The function should accept all input as parameters and return the result
5. Example: def solve(n, m): return result (not def solve(): ...)

Return only the code (in the Python programming language) as a single fenced code block, with no additional text or explanations:"""

CREATE_GUIDANCE_EASY = """Write what you think is the clearest and most efficient solution to the following problem, considering time and space complexity.

CRITICAL REQUIREMENTS:
1. Your solution MUST be a function that takes input parameters and returns the output
2. DO NOT use stdin/stdout, input(), print(), or sys.stdin/sys.stdout
3. DO NOT use any I/O operations
4. The function should accept all input as parameters and return the result
5. Example: def solve(n, m): return result (not def solve(): ...)

Return only the code (in the Python programming language) as a single fenced code block, with no additional text or explanations:"""

# Guidance texts for judging code

JUDGE_GUIDANCE_HARD = """Compare two solutions to the same problem and decide which one is better overall.

Focus your judgment on: optimal time and space complexity (Big-O); clean, readable, and idiomatic code; generic design; small, well-defined functions; concise documentation; full correctness with thorough edge-case coverage; clear error handling; and no unnecessary third-party dependencies. Consider practical performance (avoiding unnecessary allocations/copies) and natural testability.

IMPORTANT: Only consider solutions that are functions taking parameters and returning values. Reject any solution that uses stdin/stdout, input(), print(), or sys.stdin/sys.stdout."""

JUDGE_GUIDANCE_EASY = """Decide which of the two code solutions is, in your opinion, the clearest and most efficient.

IMPORTANT: Only consider solutions that are functions taking parameters and returning values. Reject any solution that uses stdin/stdout, input(), print(), or sys.stdin/sys.stdout."""