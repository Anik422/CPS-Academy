def min_operations_to_transform(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]
        
        # For each element in b, find the minimum operations required
        min_operations = 0
        for target in b:
            min_diff = float('inf')
            for num in a:
                min_diff = min(min_diff, abs(target - num))
            min_operations += min_diff
            
        results.append(min_operations)
    
    return results

# Input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    test_cases.append((n, a, b))

# Solve
results = min_operations_to_transform(t, test_cases)

# Output
for result in results:
    print(result)
