def climbing_staris(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    ways1: int = 1
    ways2: int = 2

    for num in range(3,n+1):
        result: int = ways1 + ways2
        ways1 = ways2
        ways2 = result

    return ways2


memo: dict = {}
def climbing_stairs1(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    result: int = climbing_stairs1(n-1) + climbing_stairs1(n-2)
    memo[n] = result
    return result        
      